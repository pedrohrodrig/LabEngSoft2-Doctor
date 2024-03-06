from django.db import models

# Create your models here.
class Doctor(models.Model):
    id_user = models.PositiveIntegerField(unique=True)
    full_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, unique=True, null=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    document = models.CharField(max_length=15, unique=True, blank=False, null=True)

    class Meta: 
        db_table = "doctor"