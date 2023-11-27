from checkDate.mixins.mixins import *
import re
from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from checkDate.models.models import *
from organisation.models import Filial
import pandas as pd


class MembersResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        user_fullname = row["ФИО (полное)"]
        filial = Filial.objects.get(id=1)
        user_dept_value = Department.objects.get(id=1)
        user_position_value = row["Должность"]

        if user_fullname and user_dept_value and user_position_value:  # Проверяем, что поля не пустые
            user_position, _ = Position.objects.get_or_create(
                position=user_position_value, )
            user_dept, _ = Department.objects.get_or_create(
                name=user_dept_value, filial=filial)  # Создаем объект UserDept или получаем существующий
            user_for_date, created = UserForDate.objects.update_or_create(
                full_name=user_fullname,
                defaults={
                    'dept': user_dept,
                    'position': user_position,
                }
            )

            events_for_user, _ = EventsForUser.objects.get_or_create(
                user=user_for_date,
            )

    user = fields.Field(column_name='ФИО (полное)', attribute='user',
                        widget=ForeignKeyWidget(UserForDate, 'full_name'))

    dept = fields.Field(column_name='Отдел', attribute='dept',
                        widget=ForeignKeyWidget(Department, 'name'))
    position = fields.Field(column_name='Должность', attribute='position',
                            widget=ForeignKeyWidget(Position, 'position'))

    class Meta:
        model = EventsForUser
        force_init_instance = False
        import_id_fields = ('ФИО (полное)',)
        fields = ('user', 'medicalExamination', 'knowledgeTest')


class EventsResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        medical_examination = None
        knowledge_test = None

        # Создание объектов модели MedicalExamination
        dateOfMedicalExamination = row["Дата прохождения медосмотра"]

        if dateOfMedicalExamination and dateOfMedicalExamination is not None:
            date_str = re.findall(r'\d{2}.\d{2}.\d{4}', str(dateOfMedicalExamination))
            if date_str:
                date_obj = datetime.strptime(date_str[0], '%d.%m.%Y').date()
                formatted_date = date_obj.strftime('%Y-%m-%d')
                dateOfMedicalExamination = formatted_date

        dateOfNextMedicalExamination = row["Дата следующего прохождения медосмотра"]
        try:
            period_value = row["Периодичность"]
            # Ваш код для обработки значения period_value
        except KeyError:
            # Обработка случая, когда столбец "Периодичность" отсутствует
            period_value = None
        if dateOfMedicalExamination and period_value and dateOfNextMedicalExamination:
            # Проверяем, что поля не пустые
            period, _ = Period.objects.get_or_create(name=period_value)

            # Проверяем, существует ли объект MedicalExamination с такими значениями
            medical_examination = MedicalExamination.objects.filter(
                period=period,
                dateOfMedicalExamination=dateOfMedicalExamination,
                dateOfNextMedicalExamination=dateOfNextMedicalExamination,
            ).first()

            if medical_examination is not None:
                # Обновляем атрибуты существующего объекта
                medical_examination.period = period
                medical_examination.dateOfMedicalExamination = dateOfMedicalExamination
                medical_examination.dateOfNextMedicalExamination = dateOfNextMedicalExamination
                medical_examination.save()
            else:
                # Создаем новый объект
                medical_examination = MedicalExamination.objects.create(
                    period=period,
                    dateOfMedicalExamination=dateOfMedicalExamination,
                    dateOfNextMedicalExamination=dateOfNextMedicalExamination,
                )

        # Создание объектов модели KnowledgeTest
        dateOfKnowledgeTest = row["Дата последней проверки знаний"]
        dateOfNextKnowledgeTest = row["Дата следующей проверки знаний"]

        if dateOfKnowledgeTest and period_value and dateOfNextKnowledgeTest:  # Проверяем, что поля не пустые
            period, _ = Period.objects.get_or_create(name=period_value)
            # Проверяем, существует ли объект KnowledgeTest с такими значениями
            knowledge_test = KnowledgeTest.objects.filter(
                period=period,
                dateOfKnowledgeTest=dateOfKnowledgeTest,
                dateOfNextKnowledgeTest=dateOfNextKnowledgeTest,
            ).first()

            if knowledge_test is None:
                knowledge_test, created = KnowledgeTest.objects.update_or_create(
                    period=period,
                    dateOfKnowledgeTest=dateOfKnowledgeTest,
                    dateOfNextKnowledgeTest=dateOfNextKnowledgeTest,
                    defaults={
                        'period': period,
                        'dateOfKnowledgeTest': dateOfKnowledgeTest,
                        'dateOfNextKnowledgeTest': dateOfNextKnowledgeTest,
                    }
                )

        # Создание объектов модели UserForDate
        user_fullname = row["Ф.И.О."]
        filial = Filial.objects.get(id=1)
        user_dept_value = row["Отдел"]  # Значение для поля user_dept
        user_position_value = row["Должность"]

        if user_fullname and user_dept_value and user_position_value:  # Проверяем, что поля не пустые
            user_position, _ = Position.objects.get_or_create(
                position=user_position_value, )
            user_dept, _ = Department.objects.get_or_create(
                name=user_dept_value, filial=filial)  # Создаем объект UserDept или получаем существующий
            user_for_date, created = UserForDate.objects.update_or_create(
                full_name=user_fullname,
                defaults={
                    'dept': user_dept,
                    'position': user_position,
                }
            )

            events_for_user, _ = EventsForUser.objects.update_or_create(
                user=user_for_date,
                defaults={
                    'medicalExamination': medical_examination,
                    'knowledgeTest': knowledge_test,
                }
            )

    user = fields.Field(column_name='Ф.И.О.', attribute='user',
                            widget=ForeignKeyWidget(UserForDate, 'full_name'))
    dateOfMedicalExamination = fields.Field(column_name="Дата прохождения медосмотра",
                 attribute='MedicalExamination',
                 widget=CustomDateForeignKeyWidget(MedicalExamination, 'dateOfMedicalExamination'))

    dept = fields.Field(column_name='Отдел', attribute='dept',
                        widget=ForeignKeyWidget(Department, 'name'))
    position = fields.Field(column_name='Должность', attribute='position',
                            widget=ForeignKeyWidget(Position, 'position'))
    # period_name = fields.Field(column_name='Имя', attribute='name',
    #                           widget=ForeignKeyWidget(Period, 'name'))
    # period_name = fields.Field(column_name='Периодичность', attribute='period',
    #                             widget=ForeignKeyWidget(Period, 'name'))
    #dateOfME = fields.Field(column_name="Дата прохождения медосмотра",
    #                                        attribute='dateOfMedicalExamination',
    #                                        widget=CustomDateForeignKeyWidget(MedicalExamination, 'dateOfMedicalExamination'))

    #dateOfNextME = fields.Field(column_name="Дата следующего проходения медосмотра",
    #                                            attribute='dateOfNextMedicalExamination',
    #                                            widget=ForeignKeyWidget(MedicalExamination,
    #                                                                    'dateOfNextMedicalExamination'))

    class Meta:
        model = EventsForUser
        force_init_instance = False
        import_id_fields = ('user',)
        fields = ('user', 'medicalExamination', 'knowledgeTest')

    # def dehydrate_full_title(self, EventsForUser):
    #    event_name = getattr(EventsForUser, "user", "unknown")
    #    user_name = getattr(EventsForUser.user, "full_name", "unknown")
    #    return '%s by %s' % (event_name, user_name)


class MEResource(resources.ModelResource):
    period_name = fields.Field(column_name='Имя', attribute='period',
                               widget=ForeignKeyWidget(Period, 'name'))
    # period_period = fields.Field(column_name='Период', attribute='period',
    #                             widget=ForeignKeyWidget(Period, 'period'))
    dateOfMedicalExamination = fields.Field(attribute='dateOfMedicalExamination', column_name="Дата медосмотра")
    dateOfNextMedicalExamination = fields.Field(attribute='dateOfNextMedicalExamination',
                                                column_name="Дата следующего медосмотра")

    class Meta:
        model = MedicalExamination
        import_id_fields = ()
        fields = ('period__period',)


class PeriodResource(resources.ModelResource):
    period_name = fields.Field(attribute='name', column_name='Имя')
    period = fields.Field(attribute='period', column_name='Период')

    class Meta:
        model = Period
        import_id_fields = ('period_name',)
        fields = ['period_name', 'period']


@admin.register(ImportData)
class ImportDataAdmin(admin.ModelAdmin):
    list_display = ('csv_file', 'date_added')


@admin.register(EventsForUser)
class EventsForUserAdmin(ImportExportModelAdmin):
    list_display = ('user', 'medicalExamination', 'knowledgeTest', 'knowledgeTest_dateOfKnowledgeTest', 'id')
    resource_classes = [EventsResource]
    #resource_classes = [MembersResource]

    def knowledgeTest_dateOfKnowledgeTest(self, obj):
        if obj.knowledgeTest:
            return obj.knowledgeTest.dateOfKnowledgeTest
        return None


@admin.register(MedicalExamination)
class MedicalExaminationAdmin(ImportExportModelAdmin):
    list_display = ('dateOfMedicalExamination', 'period', 'dateOfNextMedicalExamination', 'id')
    resource_classes = [MEResource]


@admin.register(KnowledgeTest)
class KnowledgeTestAdmin(admin.ModelAdmin):
    list_display = ('dateOfKnowledgeTest', 'dateOfNextKnowledgeTest', 'id')


@admin.register(Period)
class PeriodAdmin(ImportExportModelAdmin):
    list_display = ('name', 'period',)
    resource_classes = [PeriodResource]

    # import_form_class = CustomImportForm
    # confirm_form_class = CustomConfirmImportForm


#
# def get_confirm_form_initial(self, request, import_form):
#    initial = super().get_confirm_form_initial(request, import_form)
#
#    if import_form:
#        initial['period'] = import_form.cleaned_data['period']
#    return initial


@admin.register(UserForDate)
class UserForDateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'dept', 'position')
