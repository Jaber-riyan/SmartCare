from rest_framework import serializers
from . import models

class ContactUsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'