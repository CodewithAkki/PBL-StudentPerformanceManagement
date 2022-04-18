# Create your models here.
from django.db import models
from departmentalInfo.models import courses
from students.models import CustomUser

class Examination(models.Model):
    examNo=models.AutoField(primary_key=True)
    ExamName=models.CharField(max_length=100)
    marks=models.FloatField()
    def __str__(self):
        return self.ExamName

class Exam(models.Model):
    courseNo=models.ForeignKey(courses,on_delete=models.CASCADE)
    examtype=models.ForeignKey(Examination,on_delete=models.CASCADE)
    marks=models.FloatField()
    PRN_NO=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return self.PRN_NO,self.courseNo,self.examtype
class ConductedOn(models.Model):
    examNo=models.ForeignKey(Examination,on_delete=models.CASCADE)
    courseNo=models.ForeignKey(Exam,on_delete=models.CASCADE)
    fromDate=models.DateField()
    toDate=models.DateField()
    def __str__(self):
        return self.courseNo,self.courseNo