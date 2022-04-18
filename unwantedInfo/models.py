from django.db import models
from students.models import CustomUser 
# Create your models here.
class CountryCode(models.Model):
    CountryName=models.CharField(max_length=50)
    CountriesIsoCode=models.CharField(max_length=2)
    CountriesIsdCode=models.CharField(max_length=7)
    def __str__(self) :
        return self.CountryName

class otpModel(models.Model):
    otp = models.IntegerField(unique=True)
    createdAt = models.TimeField(auto_now_add=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)