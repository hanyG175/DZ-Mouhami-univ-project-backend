from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('lawyers/', LawyersListView.as_view(), name='lawyers-list'),
    path('lawyers/<int:pk>/', LawyersDetailView.as_view(), name='lawyer-detail'),
    path('profiles/', LawyersProfileListView.as_view(), name='lawyers-list'),
    path('profile/<int:pk>/', LawyersProfileDetailView.as_view(), name='lawyer-detail'),
    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='gategory-detail'),
    path('lawyers/<int:pk>/reviews/', ReviewListView.as_view(), name='reviews-list'),
    path('lawyers/<int:pk>/reviews/<review_id>', ReviewDetailView.as_view(), name='review-detail'),
    path('lawyers/<int:pk>/appointments/', AppointmentListView.as_view(), name='lawyer-appointments-list'),
    path('profile/<int:pk>/appointments/', AppointmentListView.as_view(), name='cutomer-appointments-list'),
    path('lawyers/<int:pk>/appointments/<app_id>', AppointmentDetailView.as_view(), name='lawyer-appointment-detail'),
    path('profile/<int:pk>/appointments/<app_id>', AppointmentDetailView.as_view(), name='customer-appointment-detail'),
   
]