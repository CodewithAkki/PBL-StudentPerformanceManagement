from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from departmentalInfo.models import Department , Courses, Teachers
from departmentalInfo.serializers import DepatmentSerializer , CoursesSerializer,TeacherSerializer
from rest_framework import generics
from rest_framework import filters
# Create your views here.

class DepatmentViewAPI(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = DepatmentSerializer
    queryset = Department.objects.all()

class DepartmentAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepatmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^departmentName']

class CoursesView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()

class CoursesAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^courseName']

class TeachersView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = TeacherSerializer
    queryset = Teachers.objects.all()

class TeachersAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^departmentId']
    search_fields = ['^teacherId']
    