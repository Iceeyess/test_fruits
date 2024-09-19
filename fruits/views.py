from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import generics
from .models import Fruit
from .permissions import IsNotAdmin, IsOwnerOrStaff
from .serializers import FruitSerializer



# Create your views here.

class FruitsListAPIView(generics.ListAPIView):
    serializer_class = FruitSerializer
    queryset = Fruit.objects.all()
    # permission_classes = (IsNotAdmin,)
    permission_classes = (IsAdminUser, )

class FruitsCreateAPIView(generics.CreateAPIView):
    serializer_class = FruitSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        new_fruit = serializer.save()
        new_fruit.owner = self.request.user
        new_fruit.save()



class FruitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FruitSerializer
    queryset = Fruit.objects.all()
    permission_classes = (IsOwnerOrStaff,)
    # permission_classes = (IsAdminOrReadOnly, )