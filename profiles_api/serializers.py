from django.db.models import fields
from django.http.request import validate_host
from rest_framework import serializers
from rest_framework.decorators import permission_classes
from . import models

class HelloSerializer(serializers.Serializer):
    """" Serializer a name filed for testing  our APIView"""
    name=serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self,validated_data):  
        user=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )  

        return user 



class ProfileFeedItemSerializers(serializers.ModelSerializer):
    """" serializer  profile feed Item """

    class Meta:
        model=models.ProfileFeedItem
        fields=('id','user_profile','status_text','created_on')
        extra_kwargs={'user_profile':{'read_only':True}}

