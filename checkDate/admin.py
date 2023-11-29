from checkDate.forms import CustomExportForm
import re
from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from checkDate.models.models import *
from organisation.models import Filial


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
        # dateOfMedicalExamination = row["Дата прохождения медосмотра"]
        try:
            dateOfMedicalExamination = row["Дата прохождения медосмотра"]
            # Ваш код для обработки значения period_value
        except KeyError:
            # Обработка случая, когда столбец "Периодичность" отсутствует
            dateOfMedicalExamination = None

        if dateOfMedicalExamination and dateOfMedicalExamination is not None:
            date_str = re.findall(r'\d{2}.\d{2}.\d{4}', str(dateOfMedicalExamination))
            if date_str:
                date_obj = datetime.strptime(date_str[0], '%d.%m.%Y').date()
                formatted_date = date_obj.strftime('%Y-%m-%d')
                dateOfMedicalExamination = formatted_date

        # dateOfNextMedicalExamination = row["Дата следующего прохождения медосмотра"]
        try:
            dateOfNextMedicalExamination = row["Дата следующего прохождения медосмотра"]
            # Ваш код для обработки значения period_value
        except KeyError:
            # Обработка случая, когда столбец "Периодичность" отсутствует
            dateOfNextMedicalExamination = None
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

        try:
            dateOfKnowledgeTest = row["Дата последней проверки знаний"]
        except KeyError:
            dateOfKnowledgeTest = None

        if dateOfKnowledgeTest is not None:
            date_str = re.findall(r'\d{2}.\d{2}.\d{4}', str(dateOfKnowledgeTest))
            if date_str:
                date_obj = datetime.strptime(date_str[0], '%d.%m.%Y').date()
                formatted_date = date_obj.strftime('%Y-%m-%d')
                dateOfKnowledgeTest = formatted_date

        try:
            dateOfNextKnowledgeTest = row["Дата следующей проверки знаний"]
        except KeyError:
            dateOfNextKnowledgeTest = None

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
        position_objects = [position.strip() for position in user_position_value.split('/')]
        if user_fullname and user_dept_value and user_position_value:  # Проверяем, что поля не пустые
            # user_position, _ = Position.objects.get_or_create(
            #    position=user_position_value, )
            # user_position, _ = Position.objects.bulk_create(position_objects)
            positions = []
            for position_name in position_objects:
                user_position = Position.objects.filter(position__exact=position_name).first()
                positions.append(user_position)

            user_dept, _ = Department.objects.get_or_create(name=user_dept_value,
                                                            filial=filial)  # Создаем объект UserDept или получаем существующий

            user_for_date, created = UserForDate.objects.update_or_create(
                full_name=user_fullname,
                defaults={
                    'dept': user_dept,
                }
            )

            user_for_date.position.set(positions)

            events_for_user, _ = EventsForUser.objects.update_or_create(
                user=user_for_date,
                defaults={
                    'medicalExamination': medical_examination,
                    'knowledgeTest': knowledge_test,
                }
            )

    user = fields.Field(column_name='Ф.И.О.', attribute='user',
                        widget=ForeignKeyWidget(UserForDate, 'full_name'))

    dept = fields.Field(column_name='Отдел', attribute='user__dept',
                        widget=ForeignKeyWidget(Department, 'name'))
    position = fields.Field(column_name='Должность', attribute='user__position',
                            widget=ManyToManyWidget(Position, field='position', separator='/'))

    class Meta:
        model = EventsForUser
        force_init_instance = False
        import_id_fields = ('user',)
        fields = ('user', 'knowledgeTest__dateOfKnowledgeTest', 'knowledgeTest__dateOfNextKnowledgeTest',
                  'medicalExamination__dateOfMedicalExamination', 'medicalExamination__dateOfNextMedicalExamination')


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
    # resource_classes = [MembersResource]
    export_form_class = CustomExportForm

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
    list_display = ('full_name', 'dept', 'get_positions', 'id')

    def get_positions(self, obj):
        return ", ".join([str(pos) for pos in obj.position.all()])

    get_positions.short_description = 'Выбранные должности'


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'id')
