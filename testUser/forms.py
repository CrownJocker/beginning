from django import forms
from .models import *


class InstructionModelForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = '__all__'


class InstructionCatalogModelForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['name', 'filial']
        widgets = {
            'name': forms.SelectMultiple(attrs={'class': 'select2'}),
            'filial': forms.SelectMultiple(attrs={'class': 'select2'}),
        }
