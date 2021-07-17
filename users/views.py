from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User

from .forms import RegisterForm

class Register(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = 'login.html'

    
    