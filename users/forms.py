from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "id": "exampleInputEmail1", "aria-describedby": "emailHelp",
        "placeholder": "Enter username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password", "class": "form-control", "id": "exampleInputPassword1", "placeholder": "Enter password"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "id": "username", "placeholder": "Введите имя пользователя"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password", "class": "form-control", "id": "InputPassword1", "placeholder": "Введите пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password", "class": "form-control", "id": "InputPassword2", "placeholder": "Введите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')