from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from jokes.models import Joke
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def review(request, pk):
    form = ReviewForm()
    joke = get_object_or_404(Joke, pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.joke = joke
            form.save()

        return redirect("home")