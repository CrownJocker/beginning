# Generated by Django 4.2.5 on 2023-11-16 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkDate', '0003_rename_importdare_importdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsforuser',
            name='medicalExamination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkDate.medicalexamination', verbose_name='Медосмотр'),
        ),
    ]