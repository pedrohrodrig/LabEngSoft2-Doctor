from django.db import models
from datetime import datetime
from cpf_field.models import CPFField

# Create your models here.

class Doctor(models.Model):
    id_user = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False, default="")
    date_of_birth = models.DateField(blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, unique=True, null=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    cpf = CPFField("cpf", default="")
    service = models.CharField(max_length=255, default="doctor", null=False, blank=False)
    price = models.FloatField(default=100.0)
    bio = models.CharField(max_length=255, null=False, blank=False, default="")
    is_online = models.BooleanField(default=False)
    address = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta: 
        db_table = "doctor"


class Evaluation(models.Model):
    patientId = models.PositiveIntegerField()
    name = models.CharField(max_length=255, null=False, blank=False)
    file = models.FileField(upload_to='evaluation/')
    
    def __str__(self):
        return str(self.patient) + " - File: " + str(self.id) + str(self.name)


