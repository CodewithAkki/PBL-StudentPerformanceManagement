from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
# Create your views here.
class SocialMediaAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

class SocialMediaList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^PRN_NO']
