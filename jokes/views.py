from django.shortcuts import render, redirect
from .models import Joke, Category
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from reviews.forms import ReviewForm
from . import forms

# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddJokeCreateView(CreateView):
    model = Joke
    form_class = forms.JokeForm
    template_name = 'add_jokes.html'
    success_url = reverse_lazy('addJoke')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AddCategoryCreateView(CreateView):
    model = Category
    form_class = forms.CategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('addCategory')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class JokeDetailView(DetailView):
    model = Joke
    template_name = 'joke_detail.html'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        joke = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.joke = joke
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        joke = self.object
        comments = joke.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        
        return context

@login_required
def share_joke(request, id):
    if not request.user.is_authenticated:
        return redirect("user_login") 
    joke = Joke.objects.get(id = id)
    joke.shared_jokes = request.user 
    joke.shared_condition = True
    joke.save()
    return redirect("profile")

@login_required
def like_joke(request, id):
    if not request.user.is_authenticated:
        return redirect("user_login") 
    joke = Joke.objects.get(id = id)
    joke.like+=1
    joke.shared_jokes = request.user 
    joke.save()
    return redirect("all_jokes")

def all_jokes(request, category_slug = None):
    jokes = Joke.objects.all()
    if category_slug is not None:
        categories = Category.objects.get(slug = category_slug)
        jokes = Joke.objects.filter(categories  = categories)
    categories = Category.objects.all()
    return render(request, 'show_jokes_main.html', {'jokes' : jokes, 'categories' : categories})