from django.contrib import admin
from . import models
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Register your models here.

class AppointmentAdminModel(admin.ModelAdmin):
    list_display = ['patient_name','doctor_name','appointment_status','symptoms','time','cancel']
    
    def time(self,obj):
        return obj.time.name
    
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    
    def appointment_status(self,obj):
        return obj.appointment_status
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_type == 'Running' and obj.appointment_status == 'Online':
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('appointment_mail.html',{'user' : obj.patient.user, 'doctor' : obj.doctor})
            
            email = EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()


admin.site.register(models.Appointment,AppointmentAdminModel)
