from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.ModelSerializer):
  Student_id=serializers.ReadOnlyField()
  class Meta:
    model=Student
    fields="__all__"