from rest_framework import serializers
from .models import Customer, Land, Spout, SpoutSensor, Program, LandDailyTempRecord
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = ('id', 'name', 'location', 'customers')


class SpoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spout
        fields = ('id', 'name', 'isOn', 'land', 'spoutSensor', 'url')
        depth = 1


class SpoutSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpoutSensor
        spout = SpoutSerializer(many=False)
        fields = ('id', 'spout', 'isOn', 'url')
        depth = 1


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    lands = LandSerializer(many=True)
    user = UserSerializer(many=False)
    spouts = SpoutSerializer(many=True)
    spoutSensors = SpoutSensorSerializer(many=True)

    class Meta:
        model = Customer
        fields = ('id',
                  'url',
                  'user',
                  'lands',
                  'spouts',
                  'spoutSensors'
                  'phoneNumber',
                  'isBlocked',
                  'isActivated'
                  )
        depth = 1


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'name', 'startTimeDate', 'finishTimeDate', 'url')


class LandDailyTempRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LandDailyTempRecord
        land = LandSerializer(many=False)
        fields = ('id', 'land', 'day', 'maxTemp', 'minTemp', 'url')

