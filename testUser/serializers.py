from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from ip.models import *
from users.models import CustomUser
from rest_framework.generics import get_object_or_404


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class CustomUserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'user_permissions']


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'filial', 'department', 'position']


class CustomUserEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    #def update(self, instance, validated_data):
    #    # Проверка наличия ip
    #    ip_data = validated_data.pop('ip_address') if 'ip_address' in validated_data else None
#
    #    with transaction.atomic():
    #        instance = super().update(instance, validated_data)
#
    #        # Update ip
    #        self._update_ip(instance.ip_address, ip_data)
#
    #    return instance
#
    #def _update_ip(self, ip, data):
    #    ip_serializer = IPAddressUpdateSerializer(
    #        instance=ip, data=data, partial=True
    #    )
    #    ip_serializer.is_valid(raise_exception=True)
    #    ip_serializer.save()


class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = '__all__'


class InstructionsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['name', 'filial', 'all_view']


class StepsOfInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepForInstruction
        fields = '__all__'


class StepsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepForInstruction
        fields = ['name', 'instruction', 'description', 'illustration', 'caption']
# Переделать
