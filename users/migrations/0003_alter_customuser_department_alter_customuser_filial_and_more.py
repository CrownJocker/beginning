# Generated by Django 4.2.5 on 2023-11-15 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testUser', '0004_alter_instruction_options_alter_position_options_and_more'),
        ('organisation', '0004_alter_subdepartment_name_group'),
        ('users', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='organisation.department', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='filial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='organisation.filial', verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='testUser.position', verbose_name='Должность'),
        ),
    ]
