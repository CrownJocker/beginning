from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django import forms

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_admin', 'filial', 'department'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_admin', 'position', 'filial', 'department', 'is_superuser', 'groups',
            'user_permissions')}),
        ('Important dates', {'fields': (
            'last_login', 'date_joined')
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'position', 'is_staff')



