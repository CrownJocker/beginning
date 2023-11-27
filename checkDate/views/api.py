
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
    patch=extend_schema(summary='Изменить частично М&А', tags=['М&А']),
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


@extend_schema_view(
    get=extend_schema(summary='Получение списка сотрудников', tags=['Сотрудники']),
    post=extend_schema(summary='Добавление нового сотрудника', tags=['Сотрудники']),
)
class UserForDateListCreateView(generics.ListCreateAPIView):
    queryset = UserForDate.objects.all()
    serializer_class = UserForDateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'dept', ]

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
            return UserForDateCreateSerializer
        return UserForDateSerializer


@extend_schema_view(
    get=extend_schema(summary='Сотрудник по ID', tags=['Сотрудники']),
    put=extend_schema(summary='Изменить данные сотрудника', tags=['Сотрудники']),
    patch=extend_schema(summary='Изменить частично данные сотрудника', tags=['Сотрудники']),
    delete=extend_schema(summary='Удалить сотрудника', tags=['Сотрудники']),
)
class UserForDateUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserForDate.objects.all()
    serializer_class = UserForDateCreateSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            permission_classes = [IsMembers]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


@extend_schema_view(
    get=extend_schema(summary='Получение списка медосмотров', tags=['Медосмотр']),
    post=extend_schema(summary='Добавление нового медосмотра', tags=['Медосмотр']),
)
class MEListCreateView(generics.ListCreateAPIView):
    queryset = MedicalExamination.objects.all()
    serializer_class = MESerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id',]

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
            return MECreateSerializer
        return MESerializer


@extend_schema_view(
    get=extend_schema(summary='Медосмотр по ID', tags=['Медосмотр']),
    put=extend_schema(summary='Изменить данные медосмотра', tags=['Медосмотр']),
    patch=extend_schema(summary='Изменить частично данные медосмотра', tags=['Медосмотр']),
    delete=extend_schema(summary='Удалить медосмотр', tags=['Медосмотр']),
)
class MEUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalExamination.objects.all()
    serializer_class = MESerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            permission_classes = [IsMembers]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return MECreateSerializer
        return MESerializer



@extend_schema_view(
    get=extend_schema(summary='Получение списка аттестаций', tags=['Аттестация']),
    post=extend_schema(summary='Добавление новой аттестации', tags=['Аттестация']),
)
class KTListCreateView(generics.ListCreateAPIView):
    queryset = KnowledgeTest.objects.all()
    serializer_class = KTSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id',]

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
            return KTCreateSerializer
        return KTSerializer


@extend_schema_view(
    get=extend_schema(summary='Аттестация по ID', tags=['Аттестация']),
    put=extend_schema(summary='Изменить данные аттестации', tags=['Аттестация']),
    patch=extend_schema(summary='Изменить частично данные аттестации', tags=['Аттестация']),
    delete=extend_schema(summary='Удалить аттестацию', tags=['Аттестация']),
)
class KTUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KnowledgeTest.objects.all()
    serializer_class = KTSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            permission_classes = [IsMembers]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [IsHeadOfDepartment]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return KTCreateSerializer
        return KTSerializer
