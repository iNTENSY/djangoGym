from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import User
from .forms import UserLoginForm, UserRegistrationForm


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'userforms/login.html'

    def get_success_url(self):  # Возврат пользователя на страницу, если форма прошла валидацию
        return reverse_lazy('main:main-page')


class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'userforms/registration.html'
    success_url = reverse_lazy('users:user-login')


def profile(request, pk):
    if request.user.is_authenticated:
        data = get_object_or_404(User.objects.values('username', 'date_joined'), pk=pk)
        context = {
            'user': data
        }
    else:
        context = {
            'user': 'You are not logged in'
        }
    return render(request, 'profile/profile.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:main-page')


