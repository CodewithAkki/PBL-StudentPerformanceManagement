from rest_framework import serializers
from students.models import CustomUser
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
