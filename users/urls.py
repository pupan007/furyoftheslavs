from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import Register


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    
]
