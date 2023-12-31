# Generated by Django 4.2.5 on 2023-11-15 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testUser', '0004_alter_instruction_options_alter_position_options_and_more'),
        ('organisation', '0004_alter_subdepartment_name_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Название периода')),
                ('period', models.IntegerField(blank=True, choices=[(182, 182), (365, 365), (547, 547), (730, 730), (912, 912), (1095, 1095)], null=True, verbose_name='Периодичность')),
            ],
            options={
                'verbose_name': 'Периодичность',
                'verbose_name_plural': 'Периодичности',
            },
        ),
        migrations.CreateModel(
            name='UserForDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256, verbose_name='ФИО')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organisation.department', verbose_name='Отдел')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testUser.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Что-то',
                'verbose_name_plural': 'Такое',
            },
        ),
        migrations.CreateModel(
            name='MedicalExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfMedicalExamination', models.DateField(blank=True, null=True, verbose_name='Дата прохождения медосмотра')),
                ('dateOfNextMedicalExamination', models.DateField(blank=True, null=True, verbose_name='Дата прохождения следующего медосмотра')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='checkDate.period', verbose_name='Периодичность')),
            ],
            options={
                'verbose_name': 'Медосмотр',
                'verbose_name_plural': 'Медосмотры',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfKnowledgeTest', models.DateField(blank=True, null=True, verbose_name='Дата прохождения проверки знаний')),
                ('dateOfNextKnowledgeTest', models.DateField(blank=True, null=True, verbose_name='Дата прохождения следующей проверки знаний')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='checkDate.period', verbose_name='Периодичность')),
            ],
            options={
                'verbose_name': 'Проверка знаний',
                'verbose_name_plural': 'Проверки знаний',
            },
        ),
        migrations.CreateModel(
            name='EventsForUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledgeTest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checkDate.knowledgetest', verbose_name='Проверка знаний')),
                ('medicalExamination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checkDate.medicalexamination', verbose_name='Медосмотр')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checkDate.userfordate', verbose_name='Пользователь')),
            ],
        ),
    ]
