from django.contrib import admin
from . import views
from django.urls import path,include
from .views import StaffViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'staff', StaffViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('loginstaff/', views.staffLogin),
    path('loggedinstaff/', views.loggedinStaff),
]
