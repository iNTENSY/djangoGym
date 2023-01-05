from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='user-login'),
    path('registration/', views.RegisterUser.as_view(), name='user-registration'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout')
]