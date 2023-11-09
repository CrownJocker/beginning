from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from testUser.permissions import ReadPerm


class HomePage(TemplateView):
    permission_classes = [ReadPerm]
    login_url = reverse_lazy("staff:login")
    template_name = './home/home_page.html'