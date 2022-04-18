from rest_framework import serializers
from achievementalInfo import models

class CertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Certifications 

class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Goals

class IntranshipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Intranship

class PersonalAcheivementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.PersonalAcheivement

class PersonalProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.PersonalProject

class MailstoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Milestones