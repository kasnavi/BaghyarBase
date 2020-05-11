from rest_framework import serializers
from .models import Customer, Land
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = ('id', 'name', 'location')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    lands = LandSerializer(many=True)
    user = UserSerializer(many=False)

    class Meta:
        model = Customer
        fields = ('id', 'url', 'user', 'lands', 'phoneNumber', 'isBlocked', 'isActivated')
        depth = 1


