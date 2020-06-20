from django.contrib import admin
from .models import Customer, Land, Spout, SpoutSensor, Program, Sensor, Device, SmsReceiver

admin.site.register(Customer)
admin.site.register(Land)
admin.site.register(Spout)
admin.site.register(SpoutSensor)
admin.site.register(Program)
admin.site.register(Sensor)
admin.site.register(Device)
admin.site.register(SmsReceiver)
