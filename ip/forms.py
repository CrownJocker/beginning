from django import forms
from .models import *


class IPAddressCatalogModelForm(forms.ModelForm):
    class Meta:
        model = IPAddress
        fields = ['type_subject', 'filial', 'department', 'ip_address', 'inventory_number', 'is_active']
        widgets = {
            'type_subject': forms.SelectMultiple(attrs={'class': 'select2'}),
            'filial': forms.SelectMultiple(attrs={'class': 'select2'}),
            'department': forms.SelectMultiple(attrs={'class': 'select2'}),
        }


class IPAddressModelForm(forms.ModelForm):
    class Meta:
        model = IPAddress
        fields = '__all__'


class CreateIPAddressModelForm(forms.ModelForm):
    count_ip = forms.IntegerField()

    class Meta:
        model = IPAddress
        fields = ['filial', 'department', 'start_ip', 'count_ip', 'type_subject', 'is_active']


class UpdateIPAddressModelForm(forms.ModelForm):
    class Meta:
        model = IPAddress
        fields = ['ip_address', 'filial', 'department', 'type_subject', 'inventory_number', 'is_active']