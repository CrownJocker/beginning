# Generated by Django 4.2.5 on 2023-11-11 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0002_alter_ipaddress_department_alter_ipaddress_filial_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='startip',
            options={'verbose_name': 'Начальный IP', 'verbose_name_plural': 'Начальные IP'},
        ),
        migrations.AlterModelOptions(
            name='typesubject',
            options={'verbose_name': 'Тип устройства', 'verbose_name_plural': 'Типы устройств'},
        ),
    ]
