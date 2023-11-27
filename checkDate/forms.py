from django.forms import ModelForm
from import_export.forms import ConfirmImportForm, ImportForm

from .models.models import *
from django import forms


class CustomImportForm(ImportForm):
    period = forms.ModelChoiceField(
        queryset=Period.objects.all(),
        required=True)


class CustomConfirmImportForm(ConfirmImportForm):
    period = forms.ModelChoiceField(
        queryset=Period.objects.all(),
        required=True)


class MedicalExaminationModelForm(forms.ModelForm):
    class Meta:
        model = MedicalExamination
        fields = '__all__'


class DataImportForm(ModelForm):
    class Meta:
        model = ImportData
        fields = ('csv_file',)
