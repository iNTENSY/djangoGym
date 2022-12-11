from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth

def login(request):
    error = ''
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('main-page')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'userforms/login.html', context)

def registration(request):
    error = False
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:user-login')
        else:
            error = True
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'userforms/registration.html', context)


