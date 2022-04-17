from django.db import models

# Create your models here.
class Department(models.Model):
    departmentName=models.CharField(max_length=100)
    def __str__(self):
        return self.departmentName
        