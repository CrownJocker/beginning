# Generated by Django 4.2.5 on 2023-11-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkDate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportDare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='eventsforuser',
            options={'verbose_name': 'Медосмотры и Аттестация'},
        ),
    ]
