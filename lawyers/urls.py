from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('lawyers/', LawyersListView.as_view(), name='lawyers-list'),
    path('lawyers/<int:pk>/', LawyersDetailView.as_view(), name='lawyers-detail'),
    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='gategory-detail'),
]