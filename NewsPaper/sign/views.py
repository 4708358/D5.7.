from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import 



urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade')
]
