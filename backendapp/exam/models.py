from django.db import models
from student.models import Student

# Create your models here.
class Exam(models.Model):
    exam_id= models.AutoField(primary_key=True)
    exam_name=models.CharField(blank=False,max_length=250,unique=True)

    def __str__(self):
        return self.exam_id

class Question(models.Model):
    question_id=models.AutoField(primary_key=True)
    question=models.TextField(max_length=500,blank=False,unique=True)
    option1=models.CharField(max_length=250,blank=False)
    option2=models.CharField(max_length=250,blank=False)
    option3=models.CharField(max_length=250,blank=False)
    option4=models.CharField(max_length=250,blank=False)
    correct_ans=models.CharField(max_length=250,blank=False)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)

    def __str__(self):
        return self.Question   

class Assigned(models.Model):
    assigned_id=models.AutoField(primary_key=True)
    student=models.IntegerField(blank=False)
     
    def __int__(self):
        return self.assigned_id

class Score(models.Model):
    score_id=models.AutoField(primary_key=True)
    score=models.IntegerField(blank=False,unique=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE,blank=False)
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE,blank=False)

    def __int__(self):
        return self.score_id