from django.db import models
from datetime import datetime
from cpf_field.models import CPFField

# Create your models here.
class Doctor(models.Model):
    id_user = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, unique=True, null=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    cpf = CPFField("cpf")
    document = models.CharField(max_length=15, unique=True, blank=False, null=True)

    class Meta: 
        db_table = "doctor"

class Status(models.IntegerChoices): 
        SCHEDULED = 1, "Agendada"
        DONE = 2, "Finalizada"
        CANCELLED = 3, "Cancelada"

class Appointment(models.Model): 
    id_user_professional = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    patient = models.IntegerField()
    datetime = models.DateField()
    is_online = models.BooleanField()
    cancelled = models.BooleanField(default=False)
    
    @property
    def status(self): 
        if self.cancelled: 
            return Status.CANCELLED
         
        if datetime.now() > self.datetime: 
            return Status.DONE

        return Status.SCHEDULED
        
class PaymentStatus(models.IntegerChoices): 
        SCHEDULED = 1, "Pendente"
        DONE = 2, "Pago"
        LATE = 3, "Atrasado"
class Payments(models.Model): 
     patient = models.IntegerField()
     value = models.FloatField()
     datetime = models.DateField()
     finalDate = models.DateField()
     payed = models.BooleanField(default=False)
     
     @property 
     def status(self): 
          if datetime.now() > self.finalDate: 
               return PaymentStatus.LATE
         
          if self.payed: 
               return PaymentStatus.DONE
          
          return PaymentStatus.SCHEDULED


          