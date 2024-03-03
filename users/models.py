from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserAccount(models.Model):
    PIC_CHOICES = [
        (1, 'https://img.freepik.com/free-vector/woman-portrait-wearing-cap-glasses_1308-146040.jpg'),
        (2, 'https://img.freepik.com/premium-vector/young-man-face-avater-vector-illustration-design_968209-13.jpg'),
        (3, 'https://img.freepik.com/free-vector/male-teen-cartoon-wearing-hat_1308-153378.jpg'),
        (4, 'https://img.freepik.com/premium-photo/fun-asian-teenager-animation_183364-30921.jpg'),
        (5, 'https://img.freepik.com/free-vector/portrait-shorthaired-woman_1308-134103.jpg'),
    ]
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    verify = models.BooleanField(default=False)
    pic = models.URLField(choices=PIC_CHOICES, default=3)
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def validate_pic_choices(value):
        valid_choices = [choice[0] for choice in UserAccount.PIC_CHOICES]
        if value not in valid_choices:
            raise ValidationError(f'Invalid choice for pic: {value}')
    
    # def save(self, *args, **kwargs):
    #     self.full_clean()  # Validate the model before saving
    #     super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(UserAccount, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username
    