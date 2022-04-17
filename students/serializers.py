from rest_framework import serializers
from students.models import CustomUser,SocialMedia,Languages
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=('email',
    'password',
    'is_active',
    'bio',
    'firstname',
    'lastname',
    'middelname',
    'birthdate',
    'departmentId' , 
    'address',
    'phoneNO',
    'countryCode',
    'email' ,
    'gender',
    'profilePic')
    def to_representation(self, instance):
        data=super().to_representation(instance)
        data['PRN_NO']=instance.PRN_NO
        return data

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model=SocialMedia
        fields='__all__'

class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Languages
        fields='__all__'

