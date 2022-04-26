from django.shortcuts import render
from achievementalInfo.models import Certifications,Goals,Milestones,Intranship,PersonalAcheivement,PersonalProject
from achievementalInfo.serializers import MilestonesSerializer,CertificationsSerializer,GoalsSerializer,IntranshipSerializer,PersonalAcheivementSerializer,PersonalProjectSerializer 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import filters
# Create your views here.
class CertificationsViewAPI(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = CertificationsSerializer
    queryset = Certifications.objects.all()

class CertificationsAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Certifications.objects.all()
    serializer_class = CertificationsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^CertificationName']

class GoalsViewAPI(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = GoalsSerializer
    queryset = Goals.objects.all()

class GoalsAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^CertificationName']
    
class IntranshipViewAPI(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = IntranshipSerializer
    queryset = Intranship.objects.all()

class IntranshipAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Intranship.objects.all()
    serializer_class = IntranshipSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^PRN_NO']


class PersonalAcheivementViewAPI(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = PersonalAcheivementSerializer
    queryset = PersonalAcheivement.objects.all()

class PersonalAcheivementAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PersonalAcheivement.objects.all()
    serializer_class = PersonalAcheivementSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^CertificationName']

class PersonalProjectViewAPI(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = PersonalProjectSerializer
    queryset = PersonalProject.objects.all()

class PersonalProjectAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PersonalProject.objects.all()
    serializer_class = PersonalProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^PRN_NO']

class MilestonesViewAPI(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = MilestonesSerializer
    queryset = Milestones.objects.all()

class MilestonesAPIList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Milestones.objects.all()
    serializer_class = MilestonesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^goalId']


