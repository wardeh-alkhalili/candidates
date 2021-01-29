from rest_framework import serializers
from .models import Candidate

class UserTokenSerializer(serializers.Serializer):
    """get token for user"""
    email = serializers.EmailField(required=True, max_length=150)
    password = serializers.CharField(required=True, style={'input_type': 'password'})


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id','email','full_name', 'date_of_birth','year_of_experience', 'departmnet_Id','resume')
     
    def create(self, validated_data):
        candidate = Candidate.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            date_of_birth=validated_data['date_of_birth'],
            year_of_experience=validated_data['year_of_experience'],
            departmnet_Id=validated_data['departmnet_Id'],
        )
        candidate.save()
        return candidate

class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id','email','full_name', 'date_of_birth','year_of_experience', 'departmnet_Id','resume')