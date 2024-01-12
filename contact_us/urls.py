from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # this is router for serialization

# antena
router.register('',views.ContactUsViewset)


urlpatterns = [
    path('',include(router.urls)),
]
