# Generated by Django 4.2.5 on 2023-11-11 05:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_alter_department_deptcode_and_more'),
        ('ip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddress',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organisation.department', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='filial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organisation.filial', verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='inventory_number',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Инвентарный номер'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='IP - адрес'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='start_ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ip.startip', verbose_name='Начальный IP'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='type_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ip.typesubject', verbose_name='Тип объекта'),
        ),
        migrations.AlterField(
            model_name='startip',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='startip',
            name='name',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', 'Введите значение в формате int.int.int')], verbose_name='Начальный IP'),
        ),
        migrations.AlterField(
            model_name='typesubject',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип устройства'),
        ),
    ]
