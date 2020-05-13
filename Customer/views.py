from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Land, Spout, SpoutSensor, Program, LandDailyTempRecord, \
    Sensor
from .serializers import CustomerSerializer, UserSerializer, LandSerializer,\
    SpoutSerializer, SpoutSensorSerializer, ProgramSerializer,\
    LandDailyTempRecordSerializer, SensorSerializer
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


class SensorView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# def reportTemp(request, device_id):
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


def check_land(request, land_id, program_id):
    # land_id
    # program_id
    # response: {“d”:{“sch”:1,“exp”:0,“del_sch”:0},“c”:null}
    # {"d" {"sch":"0/1 edited or added", "exp": "one of outputs has changed" \
    # , "del_sch": "a program has deleted"} "c":"error code / null"}
    return HttpResponse("")


def expected_output(request, land_id):
    # land_id
    # response: {“d”:{“o”:“111”},“c”:null}
    # {"d":{"o":"1/0 1/0 1/0 spouts are on/off"}, "c":"error"}
    return HttpResponse("")


def ask_schedule(request, land_id, program_id):
    # land_id
    # program_id
    # {“d”:{“e”: 1,“l”:“TIMESTAMP”,“s”:[{“id”:7,”st”:”2:6:19:50:02:30”,”o”:”001”}]},“c”:null}
    # {"d":{"e": "has continue", "l":"next_ip", "s":[{"id":"program_id","st": \
    # "per_weeK[2,1,0]:day_of_week[1-7]:hour:minute:hourly_duration:minute_duration" \
    # ,"o":"1/0 1/0 1/0 spouts are on/off"}, "c":"error"}
    return HttpResponse("")


def get_device_serial(request, device_id):
    # device_id
    # return device land id
    return HttpResponse("")
