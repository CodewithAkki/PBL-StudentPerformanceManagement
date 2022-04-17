from django.shortcuts import render
from rest_framework.response import Response
from unwantedInfo.serializers import CountryCodeSerializer
from unwantedInfo.models import CountryCode
#from rest_framework.views import APIView
#from rest_framework import status
#from openpyxl import Workbook, load_workbook 
from rest_framework import generics
# Create your views here.

class ImportCountryCode(generics.ListAPIView):
    queryset = CountryCode.objects.all()
    serializer_class = CountryCodeSerializer
    '''def get(self, request, *args, **kwargs):
        wb = load_workbook("grade.xlsx")
        ws = wb.active
        for row in range (2,ws.max_row+1):
                
                data=CountryCode.objects.create(
                     name=ws['A'+str(row)].value,
                    maths=ws['B'+str(row)].value,
                    science=ws['C'+str(row)].value,
                    english=ws['D'+str(row)].value
                    )
        return HttpResponse('done',row)'''
        
