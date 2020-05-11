from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    type = models.CharField('type', max_length=100)
    description = models.CharField('description', max_length=500)
    criticalLevel = models.IntegerField()

    def __str__(self):
        return self.type + "\n " + str(self.criticalLevel)

    pass


class Contract(models.Model):
    start_date = models.DateField()
    due_date = models.DateField()
    price = models.DateField()
    brought_date = models.DateField()

    def __str__(self):
        return self.due_date

    pass


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField('phone number', max_length=12)
    isBlocked = models.BooleanField('is blocked', default=False)
    isActivated = models.BooleanField('is activated', default=True)

    def __str__(self):
        return self.user.username + "_" + self.phoneNumber

    pass


class Land(models.Model):
    name = models.CharField('land name', max_length=100)
    location = models.CharField('location', max_length=100)
    customers = models.ManyToManyField(Customer, related_name='lands')

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
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='spouts')
    isOn = models.BooleanField(default=False)

    def __str__(self):
        return "spout" + self.name + "_" + self.land.name


class SpoutSensor(models.Model):
    spout = models.OneToOneField(Spout, on_delete=models.CASCADE, related_name='spoutSensor')
    isOn = models.BooleanField(default=False)

    def __str__(self):
        return "spout sensor " + self.spout.name + "_" + self.spout.land.name


class Program(models.Model):
    name = models.CharField(max_length=50, blank=True)
    spouts = models.ManyToManyField(Spout, related_name='programs')
    startTimeDate = models.DateTimeField()
    finishTimeDate = models.DateTimeField()

    def __str__(self):
        spout_list = ""
        for spout in self.spouts.all():
            spout_list += spout.name + ",_"

        return self.name \
               + "_Program:_land:_" \
               + str(self.spouts.first().land) \
               + "__spouts_" + spout_list \
               + "_" + str(self.startTimeDate) \
               + str(self.finishTimeDate)


class LandDailyTempRecord(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='tempRecord')
    day = models.DateField(auto_now=True, auto_now_add=True)
    maxTemp = models.CharField(max_length=20)
    minTemp = models.CharField(max_length=20)

    def __str__(self):
        return "tempRecord: " + self.land.name + " " + str(self.day) \
            + "maxTemp: " + str(self.maxTemp) + "minTemp: " + str(self.minTemp)

