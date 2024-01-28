from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from geopy.geocoders import Nominatim
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import *
from .serializers import *

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


class LawyersListView(APIView):
    def get(self, request, *args, **kwargs):
        data = Avocat.objects.all()
        serializer = AvocatSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AvocatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LawyersDetailView(APIView):
    def get_object(self, pk):
        try:
            return Avocat.objects.get(pk=pk)
        except Avocat.DoesNotExist:
            return None
        
    def get(self, request, pk, *args, **kwargs):
        lawyer = self.get_object(pk)
        if lawyer is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AvocatSerializer(lawyer)
        return Response(serializer.data)
    
    def put(self, request, pk, *args, **kwargs):
        lawyer = self.get_object(pk)
        if lawyer is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AvocatSerializer(lawyer, data=request.data, context={'request': request})
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

class LawyersProfileListView(APIView):
    def get(self, request, *args, **kwargs):
        data = ProfilAvocat.objects.all()
        serializer = ProfilAvocatSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProfilAvocatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LawyersProfileDetailView(APIView):
    def get_object(self, pk):
        try:
            return ProfilAvocat.objects.get(id=pk)
        except ProfilAvocat.DoesNotExist:
            return None
        
    def get(self, request, pk, *args, **kwargs):
        lawyer = self.get_object(pk)
        if lawyer is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProfilAvocatSerializer(lawyer)
        return Response(serializer.data)
    
    def put(self, request, pk, *args, **kwargs):
        lawyer = self.get_object(pk)
        if lawyer is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProfilAvocatSerializer(lawyer, data=request.data, context={'request': request})
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

class ReviewListView(APIView):
    def get(self,request,pk,  *args, **kwargs):
        
        reviews = Review.objects.filter(lawyer=pk)
        serializer = ReviewSerializer(reviews,context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ReviewDetailView(APIView):
    def get_object(self, review_id):
        try:
            return Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            return None

    def get(self, request, review_id, *args, **kwargs):
        review = self.get_object(review_id)
        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, review_id, *args, **kwargs):
        review = self.get_object(review_id)
        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id, *args, **kwargs):
        review = self.get_object(review_id)
        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AppointmentListView(APIView):
    def get(self,request,pk,  *args, **kwargs):
        
        reviews = Appointment.objects.filter(lawyer=pk)
        serializer = AppointmentSerializer(reviews,context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AppointmentDetailView(APIView):  
    def get_object(self, app_id):
        try:
            return Appointment.objects.get(pk=app_id)
        except Appointment.DoesNotExist:
            return None

    def get(self, request, app_id, *args, **kwargs):
        review = self.get_object(app_id)
        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(review)
        return Response(serializer.data)

    def put(self, request, app_id, *args, **kwargs):
        review = self.get_object(app_id)
        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, app_id, *args, **kwargs):
        review = self.get_object(app_id)
        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def Trusted_lawyers(request):
    avocat = ProfilAvocat.objects.order_by('-rating')[:3]
    serializer = ProfilAvocatSerializer(avocat, many =True) 
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    serializer = ClientSignUpSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    """
    User login view using email and password.
    """
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key, 'user': user.email})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})

class ProfilAvocatFilter(django_filters.FilterSet):
    specialisation__name = django_filters.CharFilter(field_name='avocat__specialisation__name', lookup_expr='icontains')
    langue__name = django_filters.CharFilter(field_name='avocat__langue__name', lookup_expr='icontains')
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='exact')
    adresse = django_filters.CharFilter(field_name='avocat__adresse', lookup_expr='icontains')
    class Meta:
        model = ProfilAvocat
        fields = ['specialisation__name', 'langue__name', 'rating','adresse']

class ProfilAvocatListView(ListAPIView):
    serializer_class = ProfilAvocatSerializer
    filterset_class = ProfilAvocatFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = ProfilAvocat.objects.all()
        google_maps_link = self.request.query_params.get('adresse', None)
        geolocator = Nominatim(user_agent = "city_extractor")
        try :
            location = geolocator.geocode(google_maps_link, language='en')
            if location and location.address:
                city = location.raw.get('address', {}).get('city')  # Extract city from address
                if city:
                    queryset = queryset.filter(avocat__adresse__icontains=city)
                else:
                    return  ProfilAvocat.objects.none() 

            else:
                return ProfilAvocat.objects.none() 
        except Exception as e:
            return ProfilAvocat.objects.none() 
        return queryset

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')    
