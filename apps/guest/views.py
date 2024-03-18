from django.shortcuts import redirect
from django.contrib.auth import login as auth_login, logout
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet

from .forms import SignupForm, LoginForm

from .serializers import GuestSerializer
from apps.guest.models import Guest

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
        return redirect("hotels_list")
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('hotels_list')  # Замените 'home' на имя вашего URL-маршрута для домашней страницы
                else:
                    messages.error(request, 'Неверное имя пользователя или пароль.')
                    return redirect('login')  # Замените 'login' на имя вашего URL-маршрута для страницы входа
        else:
            form = LoginForm()
        return render(request, 'guest/login.html', {'form': form})




def login_with_admin(request):
    if request.method == 'POST':
        token = request.POST.get('token')

        try:
            token_obj = Token.objects.get(key=token)
            user = token_obj.user
            if user.is_superuser:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                auth_login(request, user)
                return HttpResponseRedirect('/admin/')  # Redirect to the admin panel
        except Token.DoesNotExist:
            pass

    return render(request, 'guest/login_with_admin.html')

def logout_view(request):
    logout(request)
    return redirect('login')

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer