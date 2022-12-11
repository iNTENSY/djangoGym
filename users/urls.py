from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='user-login'),
    path('registration/', views.registration, name='user-registration'),
]