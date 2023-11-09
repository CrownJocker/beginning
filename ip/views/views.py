from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse_lazy

from organisation.models import SubDepartment
from ip.filters import IPAddressFilter
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.views.generic import *
from ip import forms
from ip.models import *


class FilterIPAddressesView(LoginRequiredMixin, View):
    def get(self, request):
        ip_address_filter = IPAddressFilter(request.GET, queryset=IPAddress.objects.all())
        filtered_ip_addresses = ip_address_filter.qs
        form = forms.IPAddressCatalogModelForm

        context = {
            'filter': ip_address_filter,
            'filtered_ip_addresses': filtered_ip_addresses,
            'form': form
        }
        return render(request, './ip/IPAddress/ip_filtered.html', context)


class IPCatalogs(LoginRequiredMixin, ListView):
    model = IPAddress
    template_name = './ip/IPAddress/ip_catalogs.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ip_is_unactive'] = IPAddress.objects.filter(is_active=False).count()
        context['ip_is_active'] = IPAddress.objects.filter(is_active=True).count()
        return context


class IPAddressBaseView:
    login_url = reverse_lazy("staff:login")
    model = IPAddress
    success_url = reverse_lazy("ip:catalog-ip")


class CreateIPAddressView(LoginRequiredMixin, CreateView):
    object = None
    model = IPAddress
    form_class = forms.CreateIPAddressModelForm
    template_name = './ip/IPAddress/ip_create.html'
    success_url = reverse_lazy("ip:catalog-ip")
    success_message = "IP-адресс успешно создан!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            start_ip_id = self.request.POST.get('start_ip')
            start_ip = StartIP.objects.get(id=start_ip_id)
            count_ip = int(self.request.POST.get('count_ip'))
            dept_id = self.request.POST.get('department')
            filial_id = self.request.POST.get('filial')
            is_active = self.request.POST.get('is_active')
            type_subject_id = self.request.POST.get('type_subject')
            filial = Filial.objects.get(id=filial_id)
            department = Department.objects.get(id=dept_id)

            existing_ips_list = IPAddress.objects.values_list('ip_address', flat=True)
            i = 0
            ip_addresses = []

            if department.filial != filial:
                form.add_error(None, 'Выбранный отдел не принадлежит выбранному филиалу.')

            if count_ip > 256:
                form.add_error(None, "Количество IP-адресов не может превышать 256.")
            else:
                while i < count_ip:
                    if i > 255:
                        form.add_error(None, "Количество IP-адресов не может превышать 256.")
                        break
                    ip = f"{start_ip}.{i}"
                    i += 1
                    if ip in existing_ips_list:
                        count_ip += 1
                    else:
                        ip_addresses.append(ip)

            is_active = bool(is_active)

            if type_subject_id == '':
                type_subject = None
            else:
                type_subject = TypeSubject.objects.get(id=type_subject_id)

            for ip in ip_addresses:
                IPAddress.objects.create(ip_address=ip, department_id=dept_id, filial_id=filial_id, is_active=is_active,
                                         type_subject=type_subject, start_ip=start_ip)

            if form.errors:
                return super().form_invalid(form)
            messages.success(self.request, self.success_message)
            return HttpResponseRedirect(self.success_url)
        else:
            return super().form_invalid(form)


class IPAddressUpdateView(LoginRequiredMixin, IPAddressBaseView, UpdateView):
    template_name = './ip/IPAddress/ip_update.html'
    form_class = forms.UpdateIPAddressModelForm
    success_message = "IP-адресс успешно изменён!"

    def form_valid(self, form):
        # Извлекаем объект, который нужно обновить, используя метод get_object()
        instance = self.get_object()

        # Получаем новый IP-адрес из сериализатора
        new_ip_address = form.cleaned_data['ip_address']

        # Проверяем принадлежность выбранного отдела выбранному филиалу
        department = form.cleaned_data['department']
        filial = form.cleaned_data['filial']
        if department and filial and department.filial != filial:
            messages.error(self.request, "Выбранный отдел не принадлежит выбранному филиалу.")
            return self.form_invalid(form)

        # Проверяем, существует ли уже такой адрес в базе данных и отличается ли предыдущий IP-адрес от нового
        if IPAddress.objects.filter(ip_address=new_ip_address).exclude(pk=instance.pk).exists():
            messages.error(self.request, "IP-адрес уже существует в базе данных.")
            return self.form_invalid(form)

        # Отправляем сообщение об успешном обновлении
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class IPAddressDeleteView(LoginRequiredMixin, IPAddressBaseView, DeleteView):
    template_name = './ip/IPAddress/ip_delete.html'
    success_message = "IP-адресс успешно удалён!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #    if 'delete_selected' in request.POST:
    #        selected_ips = request.POST.getlist('selected_ips')
    #        if selected_ips:
    #            self.model.objects.filter(pk__in=selected_ips).delete()
    #            messages.success(request, self.success_message)
    #        return redirect(self.success_url)
    #    return super().post(request, *args, **kwargs)


class IPAddressDetailView(LoginRequiredMixin, IPAddressBaseView, DetailView):
    template_name = './ip/IPAddress/ip_view.html'
    form_class = forms.IPAddressModelForm
