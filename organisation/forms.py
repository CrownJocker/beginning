from django import forms
from .models import *


class DeptModelForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class FilModelForm(forms.ModelForm):
    class Meta:
        model = Filial
        fields = '__all__'


class SubDeptModelForm(forms.ModelForm):
    class Meta:
        model = SubDepartment
        fields = '__all__'


class GroupModelForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
