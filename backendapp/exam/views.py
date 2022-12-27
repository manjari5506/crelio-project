from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Exam,Question,Assigned,Score
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializers import CourseSerializer,ExamSerializer,QuestionSerializer,AssignedSerializer,SubsSerializer,ScoreSerializer
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset= Course.objects.all()
    serializer_class=CourseSerializer

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
    


@api_view(['Get','Post'])
def getCourses(request):
    request_data = request.data
    author=request_data.get('Author')
    #print('----',request_data)
    course = Course.objects.filter(Author=author)
    content = CourseSerializer(course, many=True).data
    if content!=[]:
        return Response({"data":content},status=200)
    else:
        return Response({"message":"Invald request"},status=400)



@api_view(['Get','Post'])
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
    course=request_data.get('course')
    exams=Exam.objects.filter(Course=course)
    content=ExamSerializer(exams, many=True).data
    if content!=[]:
        return Response({"data":content},status=200)
    else:
        return Response({"message":"Invalid request"},status=400)

@api_view(['Post'])
def getQuestions(request):
    request_data=json.load(request)
    print(request_data)
    exams=Question.objects.filter(Exam=Course)
    content=QuestionSerializer(exams, many=True).data
    if content!=[]:
        return Response({"data":content},status=200)
    else:
        return Response({"message":"Invalid request"},status=400)