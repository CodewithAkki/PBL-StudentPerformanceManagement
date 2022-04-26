from django.db import models
from students.models import CustomUser
from departmentalInfo.models import Courses 
# Create your models here.
class Certifications(models.Model):	
    CertificationNo	=	models.AutoField(primary_key=True) 
    CertificationName=	models.CharField(max_length=100)	 
    DateOfCompletion=	models.DateField(blank=True,default=" ")	 
    ExpaireDate	=	 models.DateField(blank=True,default=" ")
    CerificateIdNo=	models.IntegerField(unique=True,blank=True,default=" ") 
    Certificate	=	models.URLField(max_length=200,default=" ",blank=True) 
    PRN_NO	=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return self.PRN_NO,self.CertificationName
    
class Goals(models.Model):
    GoalId	=  models.AutoField(primary_key=True)	 
    GoalName=  models.CharField(max_length=100)		 
    StartDate= models.DateField()		 
    EndDate	=  models.DateField(blank=True,default=" ")	 
    PRN_No	=  models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    attachment=models.URLField(max_length=200,default=" ",blank=True)
    def __str__(self):
        return self.PRN_No ,self.GoalName
    
class Intranship(models.Model):
    IntranshipId=models.AutoField(primary_key=True)		 
    CompanyName	=models.CharField(max_length=100)	 
    Role		=models.CharField(max_length=100)
    DateOfJoin	=models.DateField()	 
    Duration	=models.IntegerField()	 
    EndingDate	=models.IntegerField()	 
    ComplitionCertificate=models.ForeignKey(Certifications,on_delete=models.CASCADE)		 
    PRN_NO		=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return  self.PRN_NO,self.Role


class PersonalAcheivement(models.Model):
    AcheivementId=models.AutoField(primary_key=True)	 
    PRN_NO	=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    AcheivementName=models.CharField(max_length=100)	 	 
    AcadamicYear=models.IntegerField()	 
    Details	=models.CharField(max_length=500)
    Attachment=models.ForeignKey(Certifications,on_delete=models.CASCADE)
    def __str__(self):
        return self.PRN_NO,self.AcheivementName


class PersonalProject(models.Model):
    ProjectId	=models.AutoField(primary_key=True)
    ProjectName=models.CharField(max_length=100)
    Description=models.CharField(max_length=500)
    CourseNo=models.ForeignKey(Courses,on_delete=models.CASCADE,blank=True,default=" ")
    StartDate=models.DateField()
    PRN_NO=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Duration=models.IntegerField(blank=True,default=" ")
    status=models.BooleanField(default=0)
    def __str__(self):
        return self.PRN_NO,self.ProjectName

class Milestones(models.Model):
    MailstonesId=models.AutoField(primary_key=True)		 
    goalId=models.ForeignKey(Goals,on_delete=models.CASCADE)		 
    MailstoneName=models.CharField(max_length=100)		 
    Message	=models.CharField(max_length=500)
    PRN_NO=models.ForeignKey(CustomUser,on_delete=models.CASCADE)	 
    CertificationNo	=models.ForeignKey(Certifications,on_delete=models.CASCADE)	 
    AcheivementId=models.ForeignKey(PersonalAcheivement,on_delete=models.CASCADE)		 
    project=models.ForeignKey(PersonalProject,on_delete=models.CASCADE)		 
    status=models.BooleanField(default=0)
    def __str__(self):
        return self.PRN_NO,self.MailstoneName