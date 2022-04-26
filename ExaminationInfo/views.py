from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Examination , Exam , ConductedOn
from .serializers import ExaminationSerializer , ExamSerializer ,ConductedOnSerializer
from rest_framework import generics
from rest_framework import filters
# Create your views here.
class ExaminationAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = ExaminationSerializer
    queryset = Examination.objects.all()

class ExamAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    
class ConductedOnView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = ExaminationSerializer
    queryset = Examination.objects.all()

class ExaminationAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^ExamName']

class ExamAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^PRN_NO']
    
class CondutedOnAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ConductedOn.objects.all()
    serializer_class = ConductedOnSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^examNo']
    search_fields = ['^courseNo']

