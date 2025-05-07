from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils import timezone

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MenuTodayListView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        today = timezone.now().date()
        return Menu.objects.filter(date=today)
