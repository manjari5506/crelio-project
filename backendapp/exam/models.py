from django.db import models
from student.models import Student
from staff.models import Staff

# Create your models here.

# Course model
class Course(models.Model):
    Author=models.ForeignKey(Staff,on_delete=models.CASCADE)
    Course_id= models.AutoField(primary_key=True)
    Name=models.CharField(max_length=250,unique=True,blank=False)
    Description=models.TextField(max_length=2000,blank=False)

    def __str__(self):
        return self.Name

class Exam(models.Model):
    Exam_id= models.AutoField(primary_key=True)
    Exam_name=models.CharField(blank=False,max_length=250,unique=True)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.Exam_name

class Question(models.Model):
    Question_id=models.AutoField(primary_key=True)
    Question=models.TextField(max_length=500,blank=False,unique=True)
    Option1=models.CharField(max_length=250,blank=False)
    Option2=models.CharField(max_length=250,blank=False)
    Option3=models.CharField(max_length=250,blank=False)
    Option4=models.CharField(max_length=250,blank=False)
    Correct_Ans=models.CharField(max_length=250,blank=False)
    Exam=models.ForeignKey(Exam,on_delete=models.CASCADE)

    def __str__(self):
        return self.Question   

class Assigned(models.Model):
    Assigned_id=models.AutoField(primary_key=True)
    Course=models.IntegerField(blank=False,unique=True)
    Student=models.IntegerField(blank=False)
     
    def __int__(self):
        return self.Assigned_id

class Score(models.Model):
    Score_id=models.AutoField(primary_key=True)
    Score=models.IntegerField(blank=False,unique=True)
    Student_id=models.ForeignKey(Student,on_delete=models.CASCADE,blank=False)
    Exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE,blank=False)

    def __int__(self):
        return self.Score
