from django import forms
from .models import *

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'home_selected', 'phone', 'message']
