from django.db import models

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=20)
    service_description = models.TextField()
    service_image = models.ImageField(upload_to="service/images/")
    
    
    def __str__(self):
        return self.service_name
    
    # class Meta:
    #     verbose_name_plural = "Service"