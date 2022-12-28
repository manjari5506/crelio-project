from rest_framework import serializers
from .models import Course, Exam, Question, Assigned,Score

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Course
        fields="__all__"


class ExamSerializer(serializers.ModelSerializer):
    Exam_id=serializers.ReadOnlyField()
    class Meta: 
        model=Exam
        fields= "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    Exam_id=serializers.ReadOnlyField()
    class Meta: 
        model=Question
        fields= "__all__"

class AssignedSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta: 
        model=Assigned
        fields= "__all__"

class ScoreSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Score
        fields= "__all__"

class SubsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Assigned
        #fields=['Exam']
        fields="__all__"


