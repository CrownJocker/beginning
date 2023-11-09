from django.http import JsonResponse
from rest_framework.reverse import reverse_lazy
from rest_framework.utils import json

from organisation.models import SubDepartment
from .filters import InstructionFilter
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.views.generic import *
from . import forms
from .models import *


class QubeView(TemplateView):
    template_name = 'testUser/qube.html'


class Instructions(LoginRequiredMixin, ListView):
    template_name = './testUser/Instructions/Instructions.html'
    login_url = reverse_lazy("staff:login")
    model = Instruction

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['steps'] = StepForInstruction.objects.all()
        context['instructions'] = Instruction.objects.all()
        context['inst_count'] = Instruction.objects.all().count
        return context


class InstructionDetailView(LoginRequiredMixin, DetailView):
    template_name = './testUser/Instructions/detailViewInstruction.html'
    model = Instruction

    def get_context_data(self, *, object_list=None, **kwargs):
        instruction_id = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        instruction = Instruction.objects.get(id=instruction_id)
        #context['steps'] = instruction.steps.all()
        context['steps'] = StepForInstruction.objects.all()
        context['instructions'] = Instruction.objects.all()
        return context

    # def get_queryset(self):
    #    instruction_id = self.kwargs['pk']
    #    instruction = Instruction.objects.get(id=instruction_id)
    #    return instruction.steps.all()
    # success_url = 'testUser:Instructions'


class InstructionCreateView(LoginRequiredMixin, CreateView):
    template_name = './testUser/Instructions/addInstruction.html'
    form_class = forms.InstructionModelForm
    model = Instruction
    success_url = reverse_lazy('testUser:instructions')
    success_message = "Инструкция успешно создана!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class InstructionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = './testUser/Instructions/updateInstruction.html'
    form_class = forms.InstructionModelForm
    model = Instruction
    success_url = reverse_lazy('testUser:instructions')
    success_message = "Инструкция успешно изменена!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class InstructionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = './testUser/Instructions/deleteInstruction.html'
    model = Instruction
    success_url = reverse_lazy('testUser:instructions')
    success_message = "Инструкция успешно удалена!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        selected_instructions = data.get('selected_instructions', [])
        # Удалите выбранные инструкции
        Instruction.objects.filter(pk__in=selected_instructions).delete()
        return JsonResponse({'message': 'Инструкции успешно удалены'})

    #def post(self, request, *args, **kwargs):
    #    selected_instructions = request.POST.getlist('selected_instructions')  # Получаем список выбранных инструкций
#
    #    # Удаляем выбранные инструкции
    #    Instruction.objects.filter(pk__in=selected_instructions).delete()
#
    #    messages.success(self.request, self.success_message)
    #    return super().post(request, *args, **kwargs)

    #def post(self, request, *args, **kwargs):
    #    if 'delete_selected' in request.POST:
    #        selected_instructions = request.POST.getlist('selected_instructions')
    #        if selected_instructions:
    #            self.model.objects.filter(pk__in=selected_instructions).delete()
    #            messages.success(request, self.success_message)
    #        return redirect(self.success_url)
    #    return super().post(request, *args, **kwargs)


class FilterInstructionsView(LoginRequiredMixin, View):
    def get(self, request):
        instructions_filter = InstructionFilter(request.GET, queryset=Instruction.objects.all())
        filtered_instructions = instructions_filter.qs
        form = forms.InstructionModelForm

        context = {
            'filter': instructions_filter,
            'filtered_instructions': filtered_instructions,
            'form': form
        }
        return render(request, './testUser/Instructions/filtered_instructions.html', context)


class Catalogs(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['testUser.view_filial']
    login_url = reverse_lazy("staff:login")
    model = Filial
    template_name = './testUser/catalogs.html'
    success_url = reverse_lazy("testUser:catalogs")
    context_object_name = "filials"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        context['subdepartments'] = SubDepartment.objects.all()
        return context


def sdbar(request):
    return render(request, "./testUser/sidebar.html")
