from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Land, Spout, SpoutSensor, Program, LandDailyTempRecord, \
    Sensor, Device
from .serializers import CustomerSerializer, UserSerializer, LandSerializer,\
    SpoutSerializer, SpoutSensorSerializer, ProgramSerializer,\
    LandDailyTempRecordSerializer, SensorSerializer, DeviceSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import date
from rest_framework.response import Response
from rest_framework import status


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
    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    # def create(self, request, *args, **kwargs):
    #     query_dict = request.data.copy()
    #     #print(query_dict)
    #     land_id = query_dict.get('land', None)
    #     del query_dict['land']
    #     #print(land_id)
    #     land = Land.objects.get(id=land_id)
    #     #print("###" + str(land_serializer))
    #     print(str(land_id))
    #     query_dict['land'] = land
    #     print(query_dict)
    #     serializer = SensorSerializer(data=query_dict)
    #     #print(serializer)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # return super().create(request, *args, **kwargs)


class DeviceView(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


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
    lands = Land.objects.filter(id=land_id)
    if lands.count() == 0:
        return HttpResponse('Error, wrong land id')
    land = lands.first()
    spouts = land.spouts
    print(repr(spouts))
    spouts_conditions = ''
    for spout in spouts.all():
        spouts_conditions += '1' if spout.isOn is True else '0'
    os = '{'
    cs = '}'
    return HttpResponse(f'{os}"d":{os}"o":"{spouts_conditions}"{cs},"c":null{cs}')


def ask_schedule(request, land_id, program_id):
    # land_id
    # program_id
    # {“d”:{“e”: 1,“l”:“TIMESTAMP”,“s”:[{“id”:7,”st”:”2:6:19:50:02:30”,”o”:”001”}]},“c”:null}
    # {"d":{"e": "has continue", "l":"next_ip", "s":[{"id":"program_id","st": \
    # "per_weeK[2,1,0]:day_of_week[1-7]:hour:minute:hourly_duration:minute_duration" \
    # ,"o":"1/0 1/0 1/0 spouts are on/off"}, "c":"error"}
    lands = Land.objects.filter(id=land_id)
    if lands.count() == 0:
        return HttpResponse('Error, wrong land id')
    land = lands.first()
    programs = land.programs.filter(id__gte=program_id)


    return HttpResponse("")


def get_land_id(request, device_serial):
    devices = Device.objects.filter(serial=device_serial)
    print("found device quantity " + str(devices.count()))
    if devices.count() > 0:
        print("device " + str(devices.first().land.id))
        return HttpResponse(str(devices.first().land.id))
    return HttpResponse('Error, unknown serial')
