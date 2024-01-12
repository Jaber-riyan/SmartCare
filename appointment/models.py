from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime
from .constants import APPOINTMENT_STATUS, APPOINTMENT_TYPE
# Create your models here.



class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
    appointment_type = models.CharField(choices = APPOINTMENT_TYPE,max_length = 30,default="Pending")
    appointment_status = models.CharField(choices = APPOINTMENT_STATUS,max_length = 30)
    symptoms = models.TextField()
    time = models.ForeignKey(AvailableTime,on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)
    
    
    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}"
    