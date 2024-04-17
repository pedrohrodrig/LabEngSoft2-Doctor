# Generated by Django 5.0.3 on 2024-04-08 18:17

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_doctor_bio_doctor_photo_doctor_price_doctor_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.PositiveIntegerField(unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=15)),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Others')], max_length=1)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]