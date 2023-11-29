from django.forms import ModelForm
from import_export.forms import ConfirmImportForm, ImportForm, ExportForm

from .models.models import *
from django import forms


class MedicalExaminationModelForm(forms.ModelForm):
    class Meta:
        model = MedicalExamination
        fields = '__all__'


class CustomExportForm(ExportForm):
    """Customized ExportForm, with author field required."""
    dept = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=True)