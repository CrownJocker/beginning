import groups as groups
from django.contrib import admin
from . import models
from .models import *


@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'id')
    radio_fields = {'type_subject': admin.VERTICAL}


@admin.register(StartIP)
class StartIPAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(TypeSubject)
class TypeSubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
