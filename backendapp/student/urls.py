from django.contrib import admin
from django.urls import path,include
from . import views
from .views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)


urlpatterns = [
    
    path('', include(router.urls)),
    path('loginstudent/', views.studentLogin),
    path('loggedinstudent/', views.loggedinStudent),
    
]
