from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Land
from .serializers import CustomerSerializer, UserSerializer, LandSerializer
from django.contrib.auth.models import User


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LandView(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
