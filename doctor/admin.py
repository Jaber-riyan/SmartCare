from django.contrib import admin
from . import models
# Register your models here.



class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

admin.site.register(models.Specialization,SpecializationAdmin)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

admin.site.register(models.Designation,DesignationAdmin)
admin.site.register(models.AvailableTime)
admin.site.register(models.Doctor)


class ReviewAdminModel(admin.ModelAdmin):
    list_display = ['patient_name','doctor_name','rating']
    
    def patient_name(self,obj):
        return obj.reviewer.user.first_name
    
    
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    
    
admin.site.register(models.Review,ReviewAdminModel)