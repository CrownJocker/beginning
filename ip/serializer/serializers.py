from django.db import transaction
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from ip.models import *
from users.models import CustomUser


class TypeSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeSubject
        fields = '__all__'


class TypeSubjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeSubject
        fields = ['name']


class IPAddressSerializer(serializers.ModelSerializer):
    filial = serializers.SlugRelatedField(slug_field="name", read_only=True)
    department = serializers.SlugRelatedField(slug_field="name", read_only=True)
    start_ip = serializers.SlugRelatedField(slug_field="name", read_only=True)
    type_subject = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = IPAddress
        fields = '__all__'


class IPAddressCreateSerializer(serializers.ModelSerializer):
    count_ip = serializers.IntegerField()

    class Meta:
        model = IPAddress
        fields = ['filial', 'department', 'start_ip', 'type_subject', 'count_ip', 'is_active']


class IPAddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = ['ip_address', 'filial', 'department', 'inventory_number', 'type_subject', 'is_active']

    def validate(self, attrs):
        department = attrs.get('department')
        filial = attrs.get('filial')

        # Проверяем, принадлежит ли выбранный отдел выбранному филиалу
        if department and filial and department.filial != filial:
            raise serializers.ValidationError("Выбранный отдел не принадлежит выбранному филиалу.")

        return attrs

    def validate_inventory_number(self, value):
        # Проверяем, существует ли уже такой инвентарный номер в базе данных
        if value is not None and IPAddress.objects.filter(inventory_number=value).exclude(
                pk=self.instance.pk).exists():
            raise serializers.ValidationError("Инвентарный номер уже существует в базе данных.")
        return value
