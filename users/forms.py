from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email',]
        
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit is True:

            # account = User(username = username, email=email, first_name = first_name, last_name = last_name)
            # print(account)
            # account.is_active = False
            # account.save()

            user.is_active = False
            user.save()
            UserAccount.objects.create(
                user = user,
            )
        return user
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        