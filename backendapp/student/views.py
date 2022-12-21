import json
# from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from rest_framework.decorators import api_view,renderer_classes
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from.serializers import StudentSerializer
# from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@api_view(['POST'])
def studentLogin(request):
    request_data = json.load(request)
    email=request_data.get('email')
    password=request_data.get('password')
    user = Student.objects.filter(email=email,password=password,active=True)
    content = StudentSerializer(user, many=True).data
    if content!=[]:
         return Response({"email":email,"password":password},status=200)
    else:
        return Response({"message":"Invald credentials"},status=400)

@api_view(['Post'])
def loggedinStudent(request):
    request_data = json.load(request)
    email=request_data.get('email')
    password=request_data.get('password')
    user = Student.objects.filter(email=email,password=password,active=True)
    content = StudentSerializer(user, many=True).data
    if content!=[]:
         return Response({"data":content},status=200)
    else:
        return Response({"message":"Invald request"},status=400)