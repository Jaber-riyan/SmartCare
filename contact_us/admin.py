from django.contrib import admin
from . import models
# Register your models here.

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'id','phone_number','problem']

admin.site.register(models.ContactUs,ContactModelAdmin)