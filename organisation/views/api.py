from django.contrib.auth import authenticate, login, logout
from django.db.models import Count, Case, When
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics, mixins, filters
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema_view, extend_schema

from organisation.models import *
from organisation.serializer.serializers import *
from permissions.permissions import IsMembers, IsHeadOfDepartment


@extend_schema_view(
    get=extend_schema(summary='Получение данных филиала', tags=['Филиал']),
    post=extend_schema(summary='Создание нового филиала', tags=['Филиал']),
)
class FilialListCreateView(generics.ListCreateAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsMembers]
        elif self.request.method == 'POST':
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return FilialCreateSerializer
        return FilialSerializer


@extend_schema_view(
    get=extend_schema(summary='Филиал', tags=['Филиал']),
    put=extend_schema(summary='Изменить филиал', tags=['Филиал']),
    patch=extend_schema(summary='Изменить частично филиал', tags=['Филиал']),
    delete=extend_schema(summary='Удалить филиал', tags=['Филиал']),
)
class FilialUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialCreateSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            permission_classes = [IsMembers]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


@extend_schema_view(
    get=extend_schema(summary='Получение данных отдела', tags=['Отдел']),
    post=extend_schema(summary='Создание нового отдела', tags=['Отдел']),
)
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsMembers]
        elif self.request.method == 'POST':
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return DepartmentCreateSerializer
        return DepartmentSerializer


@extend_schema_view(
    get=extend_schema(summary='Отдел', tags=['Отдел']),
    put=extend_schema(summary='Изменить отдел', tags=['Отдел']),
    patch=extend_schema(summary='Изменить частично отдел', tags=['Отдел']),
    delete=extend_schema(summary='Удалить отдел', tags=['Отдел']),
)
class DepartmentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentCreateSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            permission_classes = [IsMembers]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


@extend_schema_view(
    get=extend_schema(summary='Получение данных подотдела', tags=['Подотдел']),
    post=extend_schema(summary='Создание нового подотдела', tags=['Подотдел']),
)
class SubDepartmentListCreateView(generics.ListCreateAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsMembers]
        elif self.request.method == 'POST':
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return SubDepartmentCreateSerializer
        return SubDepartmentSerializer


@extend_schema_view(
    get=extend_schema(summary='Подотдел', tags=['Подотдел']),
    put=extend_schema(summary='Изменить подотдел', tags=['Подотдел']),
    patch=extend_schema(summary='Изменить частично подотдел', tags=['Подотдел']),
    delete=extend_schema(summary='Удалить подотдел', tags=['Подотдел']),
)
class SubDepartmentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentCreateSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            permission_classes = [IsMembers]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
