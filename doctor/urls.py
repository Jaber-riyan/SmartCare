from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('list',views.DoctorSerializerView)
router.register('specialization',views.SpecializationSerializerView)
router.register('designations',views.DesignationsSerializerView)
router.register('availabletime',views.AvailableTimeSerializerView)
router.register('reviews',views.ReviewSerializerView)


urlpatterns = [
    path('',include(router.urls)),
]
