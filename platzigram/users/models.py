from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length = 200, blank = True)
    biography = models.TextField(blank = True)
    phone_number = models.CharField(max_length = 20, blank = True)

    upload_to = 'users/pictures',
    picture = models.ImageField(
              blank = True,
              null = True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
