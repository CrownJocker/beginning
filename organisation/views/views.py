from organisation.models import SubDepartment
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.views.generic import *
from organisation import forms
from organisation.models import *


class FilialBaseView:
    login_url = reverse_lazy("staff:login")
    model = Filial
    success_url = reverse_lazy("organisation:filials")


class Filials(PermissionRequiredMixin, LoginRequiredMixin, FilialBaseView, ListView):
    permission_required = ['organisation.view_filial']
    template_name = './organisation/filial/filial.html'


class FilialDetailView(LoginRequiredMixin, FilialBaseView, DetailView):
    template_name = './organisation/filial/viewFilial.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context


class FilialCreateView(LoginRequiredMixin, FilialBaseView, CreateView):
    template_name = './organisation/filial/addFilial.html'
    form_class = forms.FilModelForm
    success_message = "Филиал успешно создан!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response


class FilialUpdateView(LoginRequiredMixin, FilialBaseView, UpdateView):
    template_name = './organisation/filial/updateFilial.html'
    form_class = forms.FilModelForm
    success_message = "Филиал успешно изменён!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message


class FilialDeleteView(LoginRequiredMixin, FilialBaseView, DeleteView):
    template_name = './organisation/filial/deleteFilial.html'
    success_message = "Филиал успешно удалён!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message


class DepartmentBaseView:
    login_url = reverse_lazy("staff:login")
    model = Department
    success_url = reverse_lazy("organisation:departments")


class Departments(PermissionRequiredMixin, LoginRequiredMixin, DepartmentBaseView, ListView):
    permission_required = ['organisation.view_department']
    template_name = './organisation/department/department.html'


class DeptDetailView(LoginRequiredMixin, DepartmentBaseView, DetailView):
    template_name = './organisation/department/viewDepartment.html'
    form_class = forms.DeptModelForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subDepts'] = SubDepartment.objects.all()
        return context


class DeptCreateView(LoginRequiredMixin, DepartmentBaseView, CreateView):
    template_name = './organisation/department/addDepartment.html'
    form_class = forms.DeptModelForm
    success_message = "Отдел успешно создан!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message


class DeptUpdateView(LoginRequiredMixin, DepartmentBaseView, UpdateView):
    template_name = './organisation/department/updateDepartment.html'
    form_class = forms.DeptModelForm
    success_message = "Отдел успешно изменён!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message


class DeptDeleteView(LoginRequiredMixin, DepartmentBaseView, DeleteView):
    template_name = './organisation/department/deleteDepartment.html'
    success_message = "Отдел успешно удален!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message


class SubDepartmentBaseView:
    login_url = reverse_lazy("staff:login")
    model = SubDepartment
    success_url = reverse_lazy("organisation:subDepartments")


class SubDepartments(PermissionRequiredMixin, LoginRequiredMixin, SubDepartmentBaseView, ListView):
    permission_required = ['organisation.view_subdepartment']
    template_name = './organisation/subDept/subDepartment.html'


class SubDeptDetailView(LoginRequiredMixin, SubDepartmentBaseView, DetailView):
    template_name = './organisation/subDept/viewSubDepartment.html'
    form_class = forms.SubDeptModelForm


class SubDeptCreateView(LoginRequiredMixin, SubDepartmentBaseView, CreateView):
    template_name = './organisation/subDept/addSubDepartment.html'
    success_message = "Подотдел успешно создан!"
    form_class = forms.SubDeptModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response


class SubDeptUpdateView(LoginRequiredMixin, SubDepartmentBaseView, UpdateView):
    template_name = './organisation/subDept/updateSubDepartment.html'
    success_message = "Подотдел успешно изменён!"
    form_class = forms.SubDeptModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message


class SubDeptDeleteView(LoginRequiredMixin, SubDepartmentBaseView, DeleteView):
    template_name = './organisation/subDept/deleteSubDepartment.html'
    success_message = "Подотдел успешно удален!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message


class GroupBaseView:
    login_url = reverse_lazy("staff:login")
    model = Group
    success_url = reverse_lazy("organisation:groups")


class Groups(PermissionRequiredMixin, LoginRequiredMixin, GroupBaseView, ListView):
    permission_required = ['organisation.view_group']
    template_name = './organisation/group/group.html'


class GroupDetailView(LoginRequiredMixin, GroupBaseView, DetailView):
    template_name = './organisation/group/viewGroup.html'
    form_class = forms.GroupModelForm


class GroupCreateView(LoginRequiredMixin, GroupBaseView, CreateView):
    template_name = './organisation/group/addGroup.html'
    success_message = "Группа успешно создана!"
    form_class = forms.GroupModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response


class GroupUpdateView(LoginRequiredMixin, GroupBaseView, UpdateView):
    template_name = './organisation/group/updateGroup.html'
    form_class = forms.GroupModelForm
    success_message = "Группа успешно изменена!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message


class GroupDeleteView(LoginRequiredMixin, GroupBaseView, DeleteView):
    template_name = './organisation/group/deleteGroup.html'
    success_message = "Группа успешно удалена!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message
