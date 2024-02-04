from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

Client = get_user_model()
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields ='__all__'

# class LawyerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lawyer 
#         fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class ClientSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Client
        fields = ['email', 'first_name', 'last_name', 'mobile', 'password']

    def create(self, validated_data):
        user = Client.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mobile=validated_data['mobile'],
            password=validated_data['password']
        )
        return user 

class AvocatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avocat
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class ProfilAvocatSerializer(serializers.ModelSerializer):
    avocat = AvocatSerializer()
    class Meta:
        model = ProfilAvocat
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
# serializers.py

class CoordinatesSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

