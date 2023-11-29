from rest_framework import serializers
from checkDate.models.models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class EventsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="full_name", read_only=True)
    medicalExamination = serializers.SlugRelatedField(slug_field="dateOfMedicalExamination", read_only=True)
    knowledgeTest = serializers.SlugRelatedField(slug_field="dateOfKnowledgeTest", read_only=True)
    dept = DepartmentSerializer(source='user.dept', read_only=True)
    nextMedicalExamination = serializers.ReadOnlyField(source='medicalExamination.dateOfNextMedicalExamination')
    nextKnowledgeTest = serializers.ReadOnlyField(source='knowledgeTest.dateOfNextKnowledgeTest')

    class Meta:
        model = EventsForUser
        fields = ['user', 'dept', 'medicalExamination', 'nextMedicalExamination', 'knowledgeTest', 'nextKnowledgeTest']


class EventsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventsForUser
        fields = ['user', 'medicalExamination', 'knowledgeTest']


class UserForDateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserForDate
        fields = ['full_name', 'dept', 'position', 'status', 'order_number']


class UserForDateSerializer(serializers.ModelSerializer):
    dept = serializers.SlugRelatedField(slug_field="name", read_only=True)
    position = serializers.SlugRelatedField(slug_field="position", read_only=True)

    class Meta:
        model = UserForDate
        fields = ['full_name', 'dept', 'position']


class MESerializer(serializers.ModelSerializer):
    period = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = MedicalExamination
        fields = ['period', 'dateOfMedicalExamination', 'dateOfNextMedicalExamination']


class MECreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalExamination
        fields = ['period', 'dateOfMedicalExamination', 'dateOfNextMedicalExamination']


class KTSerializer(serializers.ModelSerializer):
    period = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = KnowledgeTest
        fields = ['period', 'dateOfKnowledgeTest', 'dateOfNextKnowledgeTest']


class KTCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeTest
        fields = ['period', 'dateOfKnowledgeTest', 'dateOfNextKnowledgeTest']
