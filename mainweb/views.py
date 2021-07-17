from django.shortcuts import render
from django.views import generic

from .models import Filler


class HomeView(generic.ListView):
    model = Filler
    template_name = 'home.html'