from rest_framework import serializers
from .models import Lawyer,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer 
        fields = '__all__'