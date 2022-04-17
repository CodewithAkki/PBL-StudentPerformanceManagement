from students.models import CustomUser
from students.serializers import studentSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
from django.db import IntegrityError
from students.models import otpModel
import datetime
from random import randint
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail


class otpViewAPIView(APIView):
    def get(self,request,pk,sotp,format = None):
        user = get_object_or_404(CustomUser.objects.all(),username = pk)
        token = Token.objects.get(user=user)
        cotp = get_object_or_404(otpModel.objects.all(),user=user)
        if cotp.otp == int(sotp):
            user.is_active = 1    #otp is verified make user active
            user.save()
            return Response({'token':token.key},status = status.HTTP_201_CREATED)
        else:
            return Response({'check otp'},status = status.HTTP_400_BAD_REQUEST)


# Create your views here.
class userAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = studentSerializer
    queryset = CustomUser.objects.all()
    
    
    

class usersList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = studentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^email']

    def post(self, request,format = None):
        user = studentSerializer(data = request.data)   #serialize data given by user
        if user.is_valid():
            user.save()
            current_user = CustomUser.objects.get(email=request.data['email'])
            current_user.set_password(request.data['password'])
            current_user.save()
            user = studentSerializer(current_user)
            end =datetime.datetime.now() - datetime.timedelta(minutes=15)
            otps = otpModel.objects.filter(createdAt__lte=end)
            otps.delete()
            if not current_user.is_active:
                try:
                    Otp = randint(100000, 999999)
                    userOTP = otpModel(otp = Otp,user=current_user)
                    userOTP.save()
                except IntegrityError as e: 
                    if 'unique constraint' in e.message:
                        Otp = randint(100000, 999999)
                        userOTP = otpModel(otp = Otp,user=current_user)
                        userOTP.save()  
                except Exception as e:
                    print(str(e))
                if current_user.email:
                    send_mail('	Your OTP for Your gols ',str(Otp),'dom.pblteam@gmail.com',[current_user.email],fail_silently=False)
            return Response(user.data,status = status.HTTP_201_CREATED)
        return Response(user.errors, status = status.HTTP_400_BAD_REQUEST)
        
            
class userpasswordupdate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def patch(self,request,id):
        queryset =CustomUser.objects.get(PRN_No=id)
        serializer_class = studentSerializer(queryset,data=request.data,partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            current_user = CustomUser.objects.get(PRN_NO=id)
            current_user.set_password(request.data['password'])
            current_user.save()    
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        queryset =CustomUser.objects.get(PRN_NO=id)
        serializer_class = studentSerializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            current_user = CustomUser.objects.get(PRN_NO=id)
            current_user.set_password(request.data['password'])
            current_user.save()
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
        
