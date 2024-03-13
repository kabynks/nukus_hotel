from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "guest/signup.html", context={"form": form})


def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('home')  # Замените 'home' на имя вашего URL-маршрута для домашней страницы
                else:
                    messages.error(request, 'Неверное имя пользователя или пароль.')
                    return redirect('login')  # Замените 'login' на имя вашего URL-маршрута для страницы входа
        else:
            form = LoginForm()
        return render(request, 'guest/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')