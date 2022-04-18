from rest_framework import serializers
from ExaminationInfo import models 
class ConductedOnSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.ConductedOn

class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Examination

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Exam
