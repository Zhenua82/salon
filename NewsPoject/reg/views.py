from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            user = form.save()
            login(request, user)
            # return redirect('Login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'News/register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'News/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Login')
