# Generated by Django 5.0.3 on 2024-04-17 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0008_remove_availabilityoccurrence_availability_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
