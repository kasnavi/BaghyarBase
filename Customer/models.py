from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .utils import send_sms


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
    name = models.CharField('name', max_length=100)
    location = models.CharField('location', max_length=100)
    customers = models.ManyToManyField(Customer, related_name='lands')
    device = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='land', blank=True, null=True)

    def __str__(self):
        return self.name + "_" + self.location

    pass


class Sensor(models.Model):

    class Meta:
        abstract = False

    type = models.CharField('sensor_type', max_length=100, default='temp', blank=True)
    value = models.CharField('value', max_length=100, default=0)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='%(class)ss')
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Sensor, self).save(*args, **kwargs)

    def __str__(self):
        return "sensor" + self.type + "_" + self.value + "_" + self.land.name


class Spout(models.Model):
    # SPOUT1 = 1
    # SPOUT2 = 2
    # SPOUT3 = 3
    # SPOUT4 = 4
    # NUMBER_CHOICES = (
    #     (SPOUT1, 'spout1'),
    #     (SPOUT2, 'spout2'),
    #     (SPOUT3, 'spout3'),
    #     (SPOUT4, 'spout4'),
    # )
    name = models.CharField('spout name', max_length=100)
    # number = models.IntegerChoices(choices=NUMBER_CHOICES)
    number = models.IntegerField()
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='spouts')
    isOn = models.BooleanField(default=False)

    def __str__(self):
        return "spout" + self.name + "_" + self.land.name

    def save(self, *args, **kw):
        sms_receivers = SmsReceiver.objects.all().filter(spout__id=self.id)
        for sms_receiver in sms_receivers:
            sms_receiver.notify(self.isOn)
        return super().save(*args, **kw)
        #for (smsReceiver : self.sms_receivers)
        #if self.spout.isOn:
        #    send_sms(self.number, "spout_on_notif", 'spout ' + self.name + ' is on')
        #else:
        #    send_sms(self.number, "spout_on_notif", 'spout ' + self.spout.name + ' is off')


class SpoutSensor(models.Model):
    spout = models.OneToOneField(Spout, on_delete=models.CASCADE, related_name='spoutSensor')
    isOn = models.BooleanField(default=False)

    def __str__(self):
        return "spout sensor " + self.spout.name + "_" + self.spout.land.name


class Program(models.Model):
    name = models.CharField(max_length=50, blank=True)
    spouts = models.ManyToManyField(Spout, related_name='programs')
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='programs')
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
    day = models.DateField()#auto_now=True, auto_now_add=True)
    maxTemp = models.CharField(max_length=20)
    minTemp = models.CharField(max_length=20)

    def __str__(self):
        return "tempRecord: " + self.land.name + " " + str(self.day) \
            + "maxTemp: " + str(self.maxTemp) + "minTemp: " + str(self.minTemp)


class SmsReceiver(models.Model):
    number = models.CharField(max_length=20)
    spout = models.ForeignKey(Spout, on_delete=models.CASCADE, related_name='sms_receivers')

    def notify(self, is_on):
        send_sms(self.number, 'notify', 'spout ' + self.spout.name + ' is ' + ('on' if is_on else 'off'))


class TempSensor(models.Model):

    temp_value = models.CharField('temp_value', max_length=100, default=0)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='tempSensors')
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TempSensor, self).save(*args, **kwargs)

    def __str__(self):
        return "Temp Sensor " + self.temp_value + "_" + self.land.name


class SoilMoistureSensor(models.Model):

    soil_moisture_value = models.CharField('soil_moisture_value', max_length=100, default=0)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='soilMoistureSensors')
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SoilMoistureSensor, self).save(*args, **kwargs)

    def __str__(self):
        return "Soil Moisture Sensor " + self.soil_moisture_value + "_" + self.land.name


class HumiditySensor(models.Model):

    humidity_value = models.CharField('humidity_value', max_length=100, default=0)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='humiditySensors')
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(HumiditySensor, self).save(*args, **kwargs)

    def __str__(self):
        return "Humidity Sensor " + self.humidity_value + "_" + self.land.name
