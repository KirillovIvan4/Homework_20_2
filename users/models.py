from django.contrib.auth.models import AbstractUser
from django.db import models
NULLBLE = {"blank": True, "null": True}

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='эл. почта')
    phone_number = models.CharField(max_length=40,verbose_name='телефон', **NULLBLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLBLE)
    country = models.CharField(max_length=40,verbose_name='страна', **NULLBLE)

    token = models.CharField(max_length=100, verbose_name='токен', **NULLBLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
