
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics, mixins, filters

from drf_spectacular.utils import extend_schema_view, extend_schema

from checkDate.models.models import *
from checkDate.serializer.serializers import *
from permissions.permissions import IsMembers, IsHeadOfDepartment


@extend_schema_view(
    get=extend_schema(summary='Получение данных об М&А', tags=['М&А']),
    post=extend_schema(summary='Создание нового М&А', tags=['М&А']),
)
class EventsListCreateView(generics.ListCreateAPIView):
    queryset = EventsForUser.objects.all()
    serializer_class = EventsSerializer
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
            return EventsCreateSerializer
        return EventsSerializer


@extend_schema_view(
    get=extend_schema(summary='М&А', tags=['М&А']),
    put=extend_schema(summary='Изменить М&А', tags=['М&А']),
    patch=extend_schema(summary='Изменить частично М&А', tags=['Филиал']),
    delete=extend_schema(summary='Удалить М&А', tags=['М&А']),
)
class EventsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventsForUser.objects.all()
    serializer_class = EventsCreateSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            permission_classes = [IsMembers]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]