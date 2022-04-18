
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models.signals import  post_save
from django.dispatch import receiver
from django.db.models.deletion import CASCADE
from rest_framework.authtoken.models import Token
from .managers import CustomUserManager
from departmentalInfo.models import Department
from unwantedInfo.models import CountryCode
import uuid
class CustomUser(AbstractUser):
    username = None
    PRN_NO =  models.AutoField(primary_key = True)
    firstname=models.CharField(max_length=50,blank=True,default=" ")
    lastname=models.CharField(max_length=50,blank=True,default=" ")
    bio = models.TextField(null=True)
    middelname=models.CharField(max_length=50,blank=True,default=" ")
    birthdate=models.CharField(max_length=50,blank=True,default=" ")
    departmentId=models.OneToOneField(Department,CASCADE,null=True,default=None)#ForeignKey
    address=models.CharField(max_length=50,blank=True,default=" ")
    phoneNO=models.CharField(max_length=50,blank=True,default=" ")
    countryCode=models.ForeignKey(CountryCode,CASCADE,null=True,default=None)#ForeignKey
    email = models.EmailField(_('email address'),unique=True)
    gender = models.CharField(max_length=7,default='M')
    profilePic = models.URLField(max_length=200,default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
    registerDate = models.DateField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance = None,created=False,**kwargs):
    if created:
        token = Token.objects.create(user=instance)
        print('Token:- ', token.key)

class otpModel(models.Model):
    otp = models.IntegerField(unique=True)
    createdAt = models.TimeField(auto_now_add=True)
    user = models.OneToOneField(CustomUser,on_delete=CASCADE)
# Create your models here.

class SocialMedia(models.Model):
    SocialMediaId = models.UUIDField(primary_key=True, default = uuid.uuid4,editable = False,unique=True)
    SocialMediaName=models.CharField(max_length=100)
    PRN_NO=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    SocialMediaLink=models.URLField(max_length=200)
    def __str__(self):
        return self.PRN_NO , self.SocialMediaName   
class Languages(models.Model):
    LanguageId=models.AutoField(primary_key=True)
    LanguageName=models.CharField(max_length=100)
    PRN_NO=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Level=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    def __str__(self):
        return self.PRN_NO , self.LanguageName , self.Level
