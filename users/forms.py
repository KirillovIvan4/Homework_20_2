from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from catalog.forms import StyleFormMixin
from config.settings import EMAIL_HOST_USER
from users.models import User

import secrets


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")



class PasswordRecoveryForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ('email',)