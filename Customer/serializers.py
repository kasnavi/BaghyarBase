from .models import Customer, Land, Spout, SpoutSensor, Program, LandDailyTempRecord, \
    Sensor, SmsReceiver, TempSensor, SoilMoistureSensor, HumiditySensor
from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class SimpleLandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = ('id', 'name', 'location', 'url')


class SensorSerializer(serializers.ModelSerializer):
    # land = SimpleLandSerializer(many=False, read_only=False)

    class Meta:
        model = Sensor
        fields = ('id', 'type', 'value', 'land', 'modified', 'created')
        extra_kwargs = {'modified': {'read_only': True}}
        # depth = 1


class TempSensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = TempSensor
        fields = ('id', 'temp_value', 'land', 'modified', 'created')
        extra_kwargs = {'modified': {'read_only': True}, 'created': {'read_only': True}}


class SoilMoistureSensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoilMoistureSensor
        fields = ('id', 'soil_moisture_value', 'land', 'modified', 'created')
        extra_kwargs = {'modified': {'read_only': True}}


class HumiditySensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumiditySensor
        fields = ('id', 'humidity_value', 'land', 'modified', 'created')
        extra_kwargs = {'modified': {'read_only': True}}


class SmsReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsReceiver
        fields = ('id', 'number', 'spout', 'url')


class SpoutSerializer(serializers.HyperlinkedModelSerializer):
    sms_receivers = SmsReceiverSerializer(many=True)

    class Meta:
        model = Spout
        fields = ('id', 'name', 'isOn', 'land', 'spoutSensor', 'sms_receivers', 'url')
        depth = 1


class SpoutSensorSerializer(serializers.HyperlinkedModelSerializer):
    spout = SpoutSerializer(many=False)

    class Meta:
        model = SpoutSensor
        fields = ('id', 'spout', 'isOn', 'url')
        depth = 1


class LandSerializer(serializers.HyperlinkedModelSerializer):
    sensors = SensorSerializer(many=True)
    spouts = SpoutSerializer(many=True)
    # spoutSensors = SpoutSensorSerializer(many=True)

    class Meta:
        model = Land
        fields = ('id',
                  'name',
                  'location',
                  'device',
                  'customers',
                  'spouts',
                  'sensors',
                  'url')
        # 'spoutSensors'
        depth = 1


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    lands = LandSerializer(many=True)
    user = UserSerializer(many=False)

    class Meta:
        model = Customer
        fields = ('id',
                  'url',
                  'user',
                  'lands',
                  'phoneNumber',
                  'isBlocked',
                  'isActivated',
                  )
        depth = 1


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        land = LandSerializer(many=False)
        fields = ('id', 'land', 'name', 'startTimeDate', 'finishTimeDate', 'url')


class LandDailyTempRecordSerializer(serializers.HyperlinkedModelSerializer):
    land = LandSerializer(many=False)

    class Meta:
        model = LandDailyTempRecord
        fields = ('id', 'land', 'day', 'maxTemp', 'minTemp', 'url')


# class DeviceSerializer(serializers.HyperlinkedModelSerializer):
#     land = LandSerializer(many=False)
#
#     class Meta:
#         model = Device
#         fields = ('id', 'serial', 'land', 'url')

