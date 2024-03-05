from django.urls import path
from . import views
 
urlpatterns = [
    path('details/<int:pk>', views.JokeDetailView.as_view(), name='joke_detail'),
    path('add-joke/', views.AddJokeCreateView.as_view(), name='addJoke'),
    path('add-category/', views.AddCategoryCreateView.as_view(), name='addCategory'),
    path("shared-jokes/<int:id>", views.share_joke, name = "share_joke_url"),
    path("liked-jokes/<int:id>", views.like_joke, name = "like_joke_url")
]