from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import *
from .serializers import *

class LawyersListView(APIView):
    def get(self, request, *args, **kwargs):
        data = Lawyer.objects.all()
        serializer = LawyerSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = LawyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LawyersDetailView(APIView):
    def get_object(self, pk):
        try:
            return Lawyer.objects.get(pk=pk)
        except Lawyer.DoesNotExist:
            return None
        
    def get(self, request, pk, *args, **kwargs):
        lawyer = self.get_object(pk)
        if lawyer is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LawyerSerializer(lawyer)
        return Response(serializer.data)
    
    def put(self, request, pk, *args, **kwargs):
        lawyer = self.get_object(pk)
        if lawyer is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LawyerSerializer(lawyer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        lawyer = self.get_object(pk)
        if lawyer is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        lawyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
