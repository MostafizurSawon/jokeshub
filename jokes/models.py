from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Joke(models.Model):
    description = models.TextField()
    like = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="categories")
    shared_jokes = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'shared')
    # liked_jokes = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'shared')
    

    def __str__(self):
        return self.description
    
    
class Comment(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    rating = models.IntegerField(verbose_name="Your Rating : ",
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    body = models.TextField(verbose_name="Your Comment : ")
    created_on = models.DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    
    def save(self, *args, **kwargs):
        # Check if the name and email fields are empty
        if not self.name or not self.email:
            # Assign the name and email of the logged-in user
            if self.joke.owner:
                self.name = self.joke.owner.first_name + ' ' + self.joke.owner.last_name
                self.email = self.joke.owner.email
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comments by {self.name}"
        