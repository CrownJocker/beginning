from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema

from ip.serializer.serializers import *


@extend_schema_view(
    get=extend_schema(summary='Получение данных об устройстве', tags=['Тип устройства']),
    put=extend_schema(summary='Изменение данных об устройстве', tags=['Тип устройства']),
    patch=extend_schema(summary='Частичное измменение данных об устройстве', tags=['Тип устройства']),
    delete=extend_schema(summary='Удаление данных об устройстве', tags=['Тип устройства']),
)
class TypeSubjectViewApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeSubject.objects.all()
    serializer_class = TypeSubjectCreateSerializer


@extend_schema_view(
    get=extend_schema(summary='Получение данных об устройстве', tags=['Тип устройства']),
    post=extend_schema(summary='Создание данных об устройстве', tags=['Тип устройства']),
)
class TypeSubjectListApi(generics.ListCreateAPIView):
    queryset = TypeSubject.objects.all()
    serializer_class = TypeSubjectSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return TypeSubjectCreateSerializer
        return TypeSubjectSerializer


@extend_schema_view(
    get=extend_schema(summary='IP-адрес', tags=['IP-адрес']),
    put=extend_schema(summary='Изменить IP-адрес', tags=['IP-адрес']),
    patch=extend_schema(summary='Изменить частично IP-адрес', tags=['IP-адрес']),
    delete=extend_schema(summary='Удалить IP-адрес', tags=['IP-адрес']),
)
class IPAddressUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressUpdateSerializer


@extend_schema_view(
    get=extend_schema(summary='IP-адрес', tags=['IP-адрес']),
    post=extend_schema(summary='Создание IP-адреса', tags=['IP-адрес']),
)
class IPAddressListCreateView(generics.ListCreateAPIView):
    serializer_class = IPAddressSerializer
    queryset = IPAddress.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'start_ip', 'filial', 'department', 'type_subject', 'ip_address']

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return IPAddressCreateSerializer
        return IPAddressSerializer

    def create(self, request, *args, **kwargs):
        start_ip_id = self.request.POST.get('start_ip')
        start_ip = StartIP.objects.get(id=start_ip_id)
        count_ip = int(self.request.POST.get('count_ip'))
        filial_id = self.request.POST.get('filial')
        dept_id = self.request.POST.get('department')
        is_active = self.request.POST.get('is_active')
        type_subject_id = self.request.POST.get('type_subject')
        filial = Filial.objects.get(id=filial_id)
        department = Department.objects.get(id=dept_id)

        existing_ips_list = IPAddress.objects.values_list('ip_address', flat=True)
        i = 0
        ip_addresses = []

        if type_subject_id == '':
            type_subject = None
        else:
            type_subject = TypeSubject.objects.get(id=type_subject_id)

        if department.filial != filial:
            raise serializers.ValidationError('Выбранный отдел не принадлежит выбранному филиалу.')

        if count_ip > 256:
            return Response({'error': "Количество IP-адресов не может превышать 256."},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            while i < count_ip:
                if i > 255:
                    return Response({'error': "Количество IP-адресов не может превышать 256."},
                                    status=status.HTTP_400_BAD_REQUEST)
                ip = f"{start_ip}.{i}"
                i += 1
                if ip in existing_ips_list:
                    count_ip += 1
                else:
                    ip_addresses.append(ip)

        is_active = bool(is_active)

        # Сохранение сгенерированных IP-адресов в базе данных
        IPAddress.objects.bulk_create([
            IPAddress(ip_address=ip, department_id=dept_id, filial_id=filial_id, is_active=is_active,
                      type_subject=type_subject, start_ip_id=start_ip_id) for ip in ip_addresses
        ])

        return Response({'success': 'IP-адреса успешно созданы'}, status=status.HTTP_201_CREATED)
