from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields= ['name','email','dob','mobile_no']
