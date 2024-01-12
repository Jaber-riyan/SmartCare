from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('list',views.PatientViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.UserRegistraionApiView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate,name='activate'),
    path('login/',views.UserLoginApiView.as_view(),name='login'),
    path('logout/',views.LogOutView.as_view(),name='logout')
]
