from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    type = models.CharField('type', max_length=100)
    description = models.CharField('description', max_length=500)
    criticality = models.IntegerField()

    def __str__(self):
        return self.type + "\n " + str(self.criticality)
    pass


class Contract(models.Model):
    startDate = models.DateField()
    dueDate = models.DateField()
    price = models.DateField()
    broughtDate = models.DateField()

    def __str__(self):
        return self.dueDate
    pass


class Land(models.Model):
    name = models.CharField('land name', max_length=100)
    location = models.CharField('location', max_length=100)
    users = models.ManyToManyField(User)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "_" + self.location
    pass


class Sensor(models.Model):
    name = models.CharField('sensor name', max_length=100)
    type = models.CharField('sensor type', max_length=100)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    value = models.CharField('value', max_length=100)

    def __str__(self):
        return "sensor" + self.type + "_" + self.name + "_" + self.land.name


class Spout(models.Model):
    name = models.CharField('spout name', max_length=100)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    isOn = models.BooleanField(default=False)

    def __str__(self):
        return "spout" + self.name + "_" + self.land.name


class SpoutSensor(models.Model):
    spout = models.ForeignKey(Spout, on_delete=models.CASCADE)
    isOn = models.BooleanField(default=False)

    def __str__(self):
        return "spout sensor " + self.spout.name + "_" + self.spout.land.name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField('phone number', max_length=12)
    isBlocked = models.BooleanField('is blocked', default=False)
    isActivated = models.BooleanField('is activated', default=True)
    lands = models.ManyToManyField(Land)

    def __str__(self):
        return self.user.username + "_" + self.phoneNumber
    pass
