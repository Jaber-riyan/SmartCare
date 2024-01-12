from rest_framework import serializers
from . import models

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    
    designation = serializers.StringRelatedField(many = True)
    # designation = serializers.HyperlinkedRelatedField(many=True, view_name='designation-detail',read_only=True)
    
    specialization = serializers.StringRelatedField(many=True)
    # specialization = serializers.HyperlinkedRelatedField(many=True,view_name='specialization-detail',read_only=True)
    
    available_time = serializers.StringRelatedField(many=True)
    # available_time = serializers.HyperlinkedRelatedField(many=True,view_name='available_time-detail',read_only=True)
    class Meta:
        model = models.Doctor
        fields = '__all__'
        
        
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'
        
        
        
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'
        
        
        
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'