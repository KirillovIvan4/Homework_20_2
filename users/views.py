import secrets

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect

from catalog.forms import StyleFormMixin
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, PasswordRecoveryForm
from users.models import User



# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


    def form_valid (self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        host = self.request.get_host()
        user.token = token
        user.save()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f"Перейдите по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class PasswordRecoveryView(TemplateView,PasswordResetView, StyleFormMixin):
    model = User
    template_name = 'users/password_recovery.html'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('users:login')

    code = secrets.token_hex(8)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        code = PasswordRecoveryView.code
        user.set_password(code)
        user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/login/'

        send_mail(
            'Восстановление пароля',
            f'Ваш новый пароль {code}, перейдите по ссылке {url}',
            EMAIL_HOST_USER,
            [user.email],
        )
        return HttpResponseRedirect('/users/login/')


# class PasswordRecovery(PasswordResetView, StyleFormMixin):
#     form_class = PasswordRecoveryForm
#     template_name = 'users/password_recovery.html'
#     success_url = reverse_lazy('users:login')
#
#     def form_valid(self, form):
#         user = form.save()
#         new_password = secrets.token_hex(16)
#         # host = self.request.get_host()
#         user.password = new_password
#         user.save()
#
#         send_mail(
#             subject='Новый пароль',
#             message=f"Ваш новый пароль: {new_password}",
#             from_email=EMAIL_HOST_USER,
#             recipient_list=[user.email],
#         )
#         return super().form_valid(form)


# def password_recovery(request, email):
#     user = get_object_or_404(User, email=email)
#     user.password  = self.new_password
#     user.save()
#     return redirect(reverse("users:login"))



    # def form_valid (request, email):
    #     user = get_object_or_404(User, email=email)
    #     new_password = secrets.token_hex(16)
    #     user.set_password(new_password)
    #     user.save()
    #     send_mail(
    #         subject='Новый пароль',
    #         message=f"Ваш новый пароль: {new_password}",
    #         from_email=EMAIL_HOST_USER,
    #         recipient_list=[user.email],
    #     )
    #     return redirect(reverse("users:login"))