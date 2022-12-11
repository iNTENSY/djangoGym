from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_avatar', null=True, blank=True)
    is_client = models.BooleanField(default=False)

