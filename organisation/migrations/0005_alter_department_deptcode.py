# Generated by Django 4.2.5 on 2023-11-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0004_alter_subdepartment_name_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='deptCode',
            field=models.CharField(blank=True, max_length=24, null=True, unique=True, verbose_name='Код отдела'),
        ),
    ]
