from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from pyexpat.errors import messages
from rest_framework.reverse import reverse_lazy
from checkDate.forms import *
from checkDate.models import *


class MedicalExaminationBaseView:
    login_url = reverse_lazy("staff:login")
    success_url = reverse_lazy("checkDate:me-ex")


class MedicalExaminations(LoginRequiredMixin, ListView):
    model = MedicalExamination
    template_name = './checkDate/Medical_Examination/medical_examinations.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEs'] = MedicalExamination.objects.all()
        return context


class CreateMedicalExaminationView(LoginRequiredMixin, CreateView):
    model = MedicalExamination
    form_class = MedicalExaminationModelForm
    template_name = './checkDate/Medical_Examination/medEx_create.html'
    success_message = "Obj успешно создан!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class MedicalExaminationUpdateView(LoginRequiredMixin, MedicalExaminationBaseView, UpdateView):
    template_name = './checkDate/Medical_Examination/me_update.html'
    model = MedicalExamination
    form_class = MedicalExaminationModelForm
    success_message = "Obj успешно изменён!"


class MedicalExaminationDeleteView(LoginRequiredMixin, MedicalExaminationBaseView, DeleteView):
    template_name = './checkDate/Medical_Examination/me_delete.html'
    model = MedicalExamination
    success_message = "Obj успешно удалён!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class MedicalExaminationDetailView(LoginRequiredMixin, MedicalExaminationBaseView, DetailView):
    template_name = './checkDate/Medical_Examination/me_view.html'
    model = MedicalExamination
    form_class = MedicalExaminationModelForm
