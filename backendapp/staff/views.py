
import json
from rest_framework import viewsets
from .models import Staff
from rest_framework.decorators import api_view,renderer_classes
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from.serializers import StaffSerializer
# from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

@api_view(['Post'])
def staffLogin(request):
    request_data = json.load(request)
    email=request_data.get('email')
    password=request_data.get('password')
    user = Staff.objects.filter(email=email,password=password,active=True)
    content = StaffSerializer(user, many=True).data
    if content!=[]:
         return Response({"email":email,"password":password},status=200)
    else:
        return Response({"message":"Invald credentials"},status=400)

@api_view(['Post'])
def loggedinStaff(request):
    request_data = json.load(request)
    email=request_data.get('email')
    password=request_data.get('password')
    user = Staff.objects.filter(email=email,password=password,active=True)
    content = StaffSerializer(user, many=True).data
    if content!=[]:
         return Response({"data":content},status=200)
    else:
        return Response({"message":"Invald request"},status=400)