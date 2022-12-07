from django.shortcuts import render
from .models import Product

def main_page(request):
    data = Product.objects.all()
    content = {
        'info': data
    }
    return render(request, 'base.html', content)

def about_page(request):
    return render(request, 'about_us/about_us.html')

def contacts_page(request):
    return render(request, 'contacts/contacts.html')

def login(request):
    return render(request, 'userforms/login.html')

def registration(request):
    return render(request, 'userforms/registration.html')