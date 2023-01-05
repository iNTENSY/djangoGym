from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', MainPage.as_view(), name='main-page'),
    path('about/', about_page, name='about-page'),
    path('contacts/', contacts_page, name='contacts-page'),
    path('product/<int:pk>/', ShowProductDetail.as_view(), name='product-detail'),
]