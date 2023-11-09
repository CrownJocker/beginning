from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'staff'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('catalogs/', views.AllCatalogs.as_view(), name='catalogs'),
]
