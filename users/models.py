from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    city = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
