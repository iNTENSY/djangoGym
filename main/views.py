from django.shortcuts import render

def main_page(request):
    return render(request, 'base.html')

def about_page(request):
    return render(request, 'about_us/about_us.html')

def contacts_page(request):
    return render(request, 'contacts/contacts.html')

def login(request):
    return render(request, 'userforms/login.html')

def registration(request):
    return render(request, 'userforms/registration.html')