from django.db import models

# Create your models here.
class CountryCode(models.Model):
    CountryName=models.CharField(max_length=50)
    CountriesIsoCode=models.CharField(max_length=2)
    CountriesIsdCode=models.CharField(max_length=7)
    def __str__(self) :
        return self.CountryName

