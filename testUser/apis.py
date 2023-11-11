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

from testUser.models import *
from testUser.serializers import *


@extend_schema_view(
    get=extend_schema(summary='Получение списка должностей', tags=['Должность']),
    post=extend_schema(summary='Создание новой должности', tags=['Должность']),
)
class PositionsListApi(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


@extend_schema_view(
    get=extend_schema(summary='Получение информации об должности', tags=['Должность']),
    put=extend_schema(summary='Изменение информации об должности', tags=['Должность']),
    patch=extend_schema(summary='Частичное изменение должности', tags=['Должность']),
    delete=extend_schema(summary='Удаление должности', tags=['Должность']),
)
class PositionsUpdateViewApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer



@extend_schema_view(
    get=extend_schema(summary='Получение списка шагов', tags=['Шаги']),
    post=extend_schema(summary='Создание нового шага', tags=['Шаги']),
)
class StepsListApi(generics.ListCreateAPIView):
    queryset = StepForInstruction.objects.all()
    serializer_class = StepsOfInstructionSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return StepsCreateSerializer
        return StepsOfInstructionSerializer


@extend_schema_view(
    get=extend_schema(summary='Получение информации об шаге', tags=['Шаги']),
    put=extend_schema(summary='Изменение информации об шаге', tags=['Шаги']),
    patch=extend_schema(summary='Частичное изменение шага', tags=['Шаги']),
    delete=extend_schema(summary='Удаление шага', tags=['Шаги']),
)
class StepsUpdateViewApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = StepForInstruction.objects.all()
    serializer_class = StepsCreateSerializer


@extend_schema_view(
    get=extend_schema(summary='Получение списка инструкций', tags=['Инструкции']),
    post=extend_schema(summary='Создание новой инструкции', tags=['Инструкции']),
)
class InstructionsListApi(generics.ListCreateAPIView):
    queryset = Instruction.objects.all()
    serializer_class = InstructionsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return InstructionsCreateSerializer
        return InstructionsSerializer


@extend_schema_view(
    get=extend_schema(summary='Получение инструкции', tags=['Инструкции']),
    put=extend_schema(summary='Изменение инструкции', tags=['Инструкции']),
    patch=extend_schema(summary='Частичное изменение инструкции', tags=['Инструкции']),
    delete=extend_schema(summary='Удаление инструкции', tags=['Инструкции']),
)
class InstructionsUpdateViewApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instruction.objects.all()
    serializer_class = InstructionsCreateSerializer


@extend_schema_view(
    get=extend_schema(summary='Получение данных текущего пользователя', tags=['Текущий пользователь']),
    put=extend_schema(summary='Изменение данных текущего пользователя', tags=['Текущий пользователь']),
    patch=extend_schema(summary='Частичное изменение данных текущего пользователя', tags=['Текущий пользователь']),
)
class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserEmployeeSerializer

    def get_object(self):
        return self.request.user


@extend_schema_view(
    get=extend_schema(summary='Получение списка пользователей', tags=['Пользователь']),
    post=extend_schema(summary='Создание пользователя', tags=['Пользователь']),
)
class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserEmployeeSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return CustomUserCreateSerializer
        return CustomUserEmployeeSerializer

