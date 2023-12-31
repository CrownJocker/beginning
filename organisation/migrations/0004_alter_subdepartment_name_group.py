# Generated by Django 4.2.5 on 2023-11-13 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0003_alter_department_options_alter_filial_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdepartment',
            name='name',
            field=models.CharField(blank=True, help_text='Добавьте название подотдела', max_length=255, unique=True, verbose_name='Название подотдела'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Добавьте название группы', max_length=255, unique=True, verbose_name='Название группы')),
                ('groupCode', models.CharField(blank=True, max_length=24, unique=True, verbose_name='Код группы')),
                ('subDept', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='group', to='organisation.subdepartment', verbose_name='Подотдел')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]
