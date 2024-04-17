# Generated by Django 5.0.3 on 2024-04-07 20:31

import cpf_field.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.IntegerField()),
                ('value', models.FloatField()),
                ('datetime', models.DateField()),
                ('finalDate', models.DateField()),
                ('payed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='cpf',
            field=cpf_field.models.CPFField(default='', max_length=14, verbose_name='cpf'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.IntegerField()),
                ('datetime', models.DateField()),
                ('is_online', models.BooleanField()),
                ('cancelled', models.BooleanField(default=False)),
                ('id_user_professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='Doctor.doctor')),
            ],
        ),
    ]