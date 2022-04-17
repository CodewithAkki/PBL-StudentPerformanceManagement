from pyexpat import model
from rest_framework import serializers
from unwantedInfo.models import CountryCode
class CountryCodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CountryCode