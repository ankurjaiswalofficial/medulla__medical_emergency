from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'phone_number', 'password1', 'password2']


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    password = forms.CharField(max_length=255)
