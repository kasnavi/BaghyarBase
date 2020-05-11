from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Land, Spout, SpoutSensor, Program, LandDailyTempRecord
from .serializers import CustomerSerializer, UserSerializer, LandSerializer,\
    SpoutSerializer, SpoutSensorSerializer, ProgramSerializer,\
    LandDailyTempRecordSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import date


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LandView(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer


class SpoutView(viewsets.ModelViewSet):
    queryset = Spout.objects.all()
    serializer_class = SpoutSerializer


class SpoutSensorView(viewsets.ModelViewSet):
    queryset = SpoutSensor.objects.all()
    serializer_class = SpoutSensorSerializer


class ProgramView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class LandDailyTempRecordView(viewsets.ModelViewSet):
    queryset = LandDailyTempRecord.objects.all()
    serializer_class = LandDailyTempRecordSerializer


# def ReportTemp(request, device_id):
#     temp = request.Get['temp']
#     today = date.today()
#     tempRecord = LandDailyTempRecord.objects.filter(land__id=device_id, day=today)
#     if tempRecord.count() > 0:
#         record = tempRecord[0]
#         record.addTemp(temp)
#     else:
#         record = LandDailyTempRecord.CreateRecord(Land.objects.filter(id=device_id), today, temp)
#
#     record.save()
#
#
#
#     return HttpResponse("")

