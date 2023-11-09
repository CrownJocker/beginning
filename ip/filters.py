import django_filters
from django import forms
from .models import *
from django_select2.forms import Select2MultipleWidget


# class IPAddressFilter(django_filters.FilterSet):
#    filial = django_filters.MultipleChoiceFilter(field_name='filial')
#    department = django_filters.MultipleChoiceFilter(field_name='department')
#    class Meta:
#        model = IPAddress
#        fields = ['type_subject', 'filial', 'department', 'is_active']
#       # fields = {
#       #     'type_subject': ['exact'],
#       #     'filial': ['exact'],
#       #     'department': ['exact'],
#       #     'is_active': ['exact'],
#       # }

#class IPAddressFilter(django_filters.FilterSet):
#    type_subject = django_filters.ModelMultipleChoiceFilter(
#        field_name='type_subject',
#        queryset=TypeSubject.objects.all(),
#        widget=Select2MultipleWidget,
#    )
#    filial = django_filters.ModelMultipleChoiceFilter(
#        label='filial',
#        queryset=Filial.objects.all(),
#        widget=Select2MultipleWidget,
#    )
#    department = django_filters.ModelMultipleChoiceFilter(
#        label='department',
#        queryset=Department.objects.all(),
#        widget=Select2MultipleWidget,
#    )
#    is_active = django_filters.BooleanFilter(widget=forms.CheckboxInput, field_name='is_active')
#
#    class Meta:
#        model = IPAddress
#        fields = ['type_subject', 'filial', 'department', 'is_active']
#
#class IPAddressFilterForm(forms.Form):
#    type_subject = forms.ModelChoiceField(queryset=TypeSubject.objects.all(), required=False, empty_label="All")
#    filial = forms.ModelChoiceField(queryset=Filial.objects.all(), required=False, empty_label="All")
#    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False, empty_label="All")
#
#    def __init__(self, *args, **kwargs):
#        super(IPAddressFilterForm, self).__init__(*args, **kwargs)
#        self.fields['type_subject'].widget.attrs.update({'class': 'form-control'})
#        self.fields['filial'].widget.attrs.update({'class': 'form-control'})
#        self.fields['department'].widget.attrs.update({'class': 'form-control'})

#class IPAddressFilter(django_filters.FilterSet):
#    ip_address = django_filters.CharFilter(lookup_expr='icontains', label='IP Address')
#    inventory_number = django_filters.NumberFilter(label='Inventory Number')
#    is_active = django_filters.BooleanFilter(label='Is Active')
#    filial = django_filters.ModelMultipleChoiceFilter(
#        label='filial',
#        queryset=Filial.objects.all(),
#        widget=Select2MultipleWidget,
#    )
#    department = django_filters.ModelMultipleChoiceFilter(
#        label='department',
#        queryset=Department.objects.all(),
#        widget=Select2MultipleWidget,
#    )
#
#    class Meta:
#        model = IPAddress
#        fields = ['ip_address', 'inventory_number', 'is_active', 'filial', 'department']
class IPAddressFilter(django_filters.FilterSet):
    ip_address = django_filters.CharFilter(lookup_expr='icontains', label='IP Address')
    inventory_number = django_filters.NumberFilter(label='Inventory Number')
    is_active = django_filters.BooleanFilter(label='Is Active')
    type_subject = django_filters.ModelMultipleChoiceFilter(
        queryset=TypeSubject.objects.all(),
        widget=Select2MultipleWidget
    )
    filial = django_filters.ModelMultipleChoiceFilter(
        queryset=Filial.objects.all(),
        widget=Select2MultipleWidget
    )
    department = django_filters.ModelMultipleChoiceFilter(
        queryset=Department.objects.all(),
        widget=Select2MultipleWidget
    )

    class Meta:
        model = IPAddress
        fields = ['ip_address', 'inventory_number', 'is_active', 'type_subject', 'filial', 'department']


