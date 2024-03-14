from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Guest

class SignupForm(UserCreationForm):
    class Meta:
        model = Guest
        fields = ['username', 'first_name','last_name', 'email', "phone_number", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)