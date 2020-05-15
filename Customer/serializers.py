from .models import Customer, Land, Spout, SpoutSensor, Program, LandDailyTempRecord, \
    Sensor, Device
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
    land = SimpleLandSerializer(many=False, read_only=False)

    class Meta:
        model = Sensor
        fields = ('id', 'type', 'value', 'land', 'modified', 'created', 'url')
        extra_kwargs = {'modified': {'read_only': True}}
        depth = 1


class SpoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spout
        fields = ('id', 'name', 'isOn', 'land', 'spoutSensor', 'url')
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


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    land = LandSerializer(many=False)

    class Meta:
        model = Device
        fields = ('id', 'serial', 'land', 'url')

