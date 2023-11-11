from django.contrib import admin
from .models import *


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ('name', 'filialCode','id')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'deptCode', 'id')


@admin.register(SubDepartment)
class SubDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subDeptCode', 'id')
