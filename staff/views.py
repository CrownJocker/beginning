from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic import *
from django.urls import reverse_lazy

import testUser
from .models import *


class AllCatalogs(ListView):
    login_url = reverse_lazy("staff:login")
    model = testUser.models.Filial
    template_name = './staff/catalogs.html'


class LoginView(auth_views.LoginView):
    template_name = 'staff/login.html'


class LogoutView(auth_views.LogoutView):
    template_name = 'staff/logout.html'
    login_url = reverse_lazy("staff:login")
    success_url = reverse_lazy("staff:login")
