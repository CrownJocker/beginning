# Generated by Django 4.2.5 on 2023-11-21 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkDate', '0006_alter_eventsforuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsforuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='checkDate.userfordate', verbose_name='Пользователь'),
        ),
    ]
