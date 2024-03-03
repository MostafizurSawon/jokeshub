from django.urls import path
from . import views
 
urlpatterns = [
    path('give-review/<int:pk>', views.review, name='review'),
]