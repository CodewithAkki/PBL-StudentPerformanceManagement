from rest_framework import serializers
from departmentalInfo.models import Department,Courses,Teachers

class DepatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teachers
        fields='__all__' 

