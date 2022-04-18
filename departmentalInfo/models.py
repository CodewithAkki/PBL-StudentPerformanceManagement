from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Department(models.Model):
    departmentName=models.CharField(max_length=100)
    def __str__(self):
        return self.departmentName

class Courses(models.Model):
    courseNo=models.AutoField(primary_key=True)
    courseName=models.CharField(max_length=100)
    departmentId=models.ForeignKey('Department',on_delete=models.CASCADE)
    def __str__(self):
        return self.courseName

class Teachers(models.Model):
    teacherId=models.AutoField(primary_key=True)
    departmentId=models.ForeignKey('Department',on_delete=models.CASCADE)
    firstName=models.CharField(max_length=100)
    middelName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    email=models.EmailField(_('email address'),unique=True)
    spacalizedIn=models.CharField(max_length=100)
    def __str__(self):
        return self.email