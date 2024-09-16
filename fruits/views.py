from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from .models import Fruit
from .serializers import FruitSerializer



# Create your views here.

class FruitsListAPIView(generics.ListAPIView):
    serializer_class = FruitSerializer
    queryset = Fruit.objects.all()

class FruitsCreateAPIView(generics.CreateAPIView):
    serializer_class = FruitSerializer

class FruitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FruitSerializer
    queryset = Fruit.objects.all()
    permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAdminOrReadOnly, )