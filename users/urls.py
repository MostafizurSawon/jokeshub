from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout, profile, activate
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('activate/<uid64>/<token>/', activate, name = 'activate'),
]
