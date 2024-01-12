from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    user = models.OneToOneField(User, related_name="user",on_delete=models.CASCADE,null=True,blank=True)
    user_phone_number = models.CharField(max_length=12,null=True,blank=True)
    user_image = models.ImageField(upload_to="patient/images/",null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    