from django import forms
from .models import Joke, Category, Comment
# from .models import Joke, Comment

class JokeForm(forms.ModelForm):
    class Meta: 
        model = Joke
        # fields = '__all__'
        exclude = ['like','owner','created_on', 'shared_jokes']
    
        
class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = '__all__'
        # exclude = ['slug']
        
class CommentForm(forms.ModelForm):
    # name = Joke.owner
    class Meta: 
        model = Comment
        # fields = '__all__'
        fields = ['rating','body']
