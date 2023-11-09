from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from organisation.models import *
from users.models import CustomUser


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = '__all__'


class FilialCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = ['name', 'filialCode', 'description']


class DepartmentSerializer(serializers.ModelSerializer):
    filial = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['filial', 'name', 'deptCode', 'description']


class SubDepartmentSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = SubDepartment
        fields = '__all__'


class SubDepartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartment
        fields = ['department', 'name', 'subDeptCode']
