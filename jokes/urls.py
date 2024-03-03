from django.urls import path
from . import views
 
urlpatterns = [
    path('details/<int:pk>', views.JokeDetailView.as_view(), name='joke_detail'),
    # path('review/<int:pk>', views.JokeReviewView.as_view(), name='joke_review'),
    path('add-joke/', views.AddJokeCreateView.as_view(), name='addJoke'),
    path('add-category/', views.AddCategoryCreateView.as_view(), name='addCategory'),
    # path('review/<int:pk>', views.JokeReviewView.as_view(), name='borrowed_book'),
    path("shared-jokes/<int:id>", views.share_joke, name = "share_joke_url")
]
# urlpatterns = [
#     path('details/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
#     path('user-borrowed-books/<int:pk>', views.BorrowBook, name="borrow_book"),
#     path("return-book/<int:pk>", views.ReturnBook, name="return_book")
# ]