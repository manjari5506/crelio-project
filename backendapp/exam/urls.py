from django.contrib import admin
from . import views
from django.urls import path,include
from .views import CourseViewSet,ExamViewSet,QuestionViewSet,AssignedViewSet,ScoreViewSet
from rest_framework import routers





router=routers.DefaultRouter()
router.register(r'course',CourseViewSet)
router.register(r'exam',ExamViewSet)
router.register(r'question',QuestionViewSet)
router.register(r'assign',AssignedViewSet)
router.register(r'score',ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getcourses/', views.getCourses),
    path('getsubscribed/', views.getassigned),
    path('getassignedexam/', views.getassignedexam),
    path('getquestions/', views.getQuestions),
]
