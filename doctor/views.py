from django.shortcuts import render
from rest_framework import serializers
from . import models
from . import serializers
from rest_framework import viewsets, filters,pagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.


class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = 'page_size'
    max_page_size = 100
    

class DoctorSerializerView(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']
    pagination_class = DoctorPagination
    
    
class DesignationsSerializerView(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    
    
class SpecializationSerializerView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set,view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

    
class AvailableTimeSerializerView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]
    
    
class ReviewSerializerView(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
