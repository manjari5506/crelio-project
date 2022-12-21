from rest_framework import serializers
from .models import Exam,Question,Assigned,Score

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    exam_id=serializers.ReadOnlyField()
    class Meta: 
        model=Exam
        fields= "__all__"

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    exam_id=serializers.ReadOnlyField()
    class Meta: 
        model=Question
        fields= "__all__"

class AssignedSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta: 
        model=Assigned
        fields= "__all__"

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model=Score
        fields= "__all__"

class SubsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Assigned
        fields=['Exam']

