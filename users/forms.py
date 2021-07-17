from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# from myapp.models import Profile

class RegisterForm(UserCreationForm):
    nick = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'nick', 'first_name', 'last_name',]