from django.shortcuts import render
from .models import CustomUser
from django.views.generic import *
from django import forms

class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'users_list.html'
