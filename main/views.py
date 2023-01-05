from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView


class MainPage(ListView):
    model = Product
    template_name = 'base.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.all().values('title', 'price', 'pk', 'category__name')


class ShowProductDetail(DetailView):
    model = Product
    template_name = 'product_detail/product_detail.html'
    context_object_name = 'item'


def about_page(request):
    return render(request, 'about_us/about_us.html')

def contacts_page(request):
    return render(request, 'contacts/contacts.html')

def login(request):
    return render(request, 'userforms/login.html')

def registration(request):
    return render(request, 'userforms/registration.html')