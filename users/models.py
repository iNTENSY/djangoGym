from django.db import models
from django.contrib.auth.models import AbstractUser

# class Category(models.Model):
#

class User(AbstractUser):
    image = models.ImageField('Личное фото пользователя', upload_to='users_avatar', null=True, blank=True)
    is_client = models.BooleanField('Клиент?', default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

