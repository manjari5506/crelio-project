from django.shortcuts import render
from rest_framework import viewsets
from .models import Exam,Question,Assigned,Score
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializers import ExamSerializer,QuestionSerializer,AssignedSerializer,SubsSerializer,ScoreSerializer
# Create your views here.

class ExamViewSet(viewsets.ModelViewSet):
    queryset= Exam.objects.all()
    serializer_class=ExamSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset= Question.objects.all()
    serializer_class=QuestionSerializer

class AssignedViewSet(viewsets.ModelViewSet):
    queryset=Assigned.objects.all()
    serializer_class=AssignedSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset=Score.objects.all()
    serializer_class=ScoreSerializer
    

@api_view(['Post'])
def getassigned(request):
    request_data=json.load(request)
    student=request_data.get('Student')
    subscribed=Assigned.objects.filter(Student=student)
    content=SubsSerializer(subscribed, many=True).data
    if content!=[]:
        return Response({"data":content},status=200)
    else:
        return Response({"message":"Invalid request"},status=400)

@api_view(['Post'])
def getassignedexam(request):
    request_data=json.load(request)
    exams=Exam.objects.filter(Exam=exam)
    content=ExamSerializer(exams, many=True).data
    if content!=[]:
        return Response({"data":content},status=200)
    else:
        return Response({"message":"Invalid request"},status=400)

@api_view(['Post'])
def getQuestions(request):
    request_data=json.load(request)
    exams=Question.objects.filter(Exam=course)
    content=QuestionSerializer(exams, many=True).data
    if content!=[]:
        return Response({"data":content},status=200)
    else:
        return Response({"message":"Invalid request"},status=400)