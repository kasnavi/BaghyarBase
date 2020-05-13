from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('customer', views.CustomerView)
router.register('user', views.UserViewSet)
router.register('land', views.LandView)
router.register('spout', views.SpoutView)
router.register('spoutSensor', views.SpoutSensorView)
router.register('program', views.ProgramView)
router.register('landDailyTempRecord', views.LandDailyTempRecordView)
router.register('sensor', views.SensorView)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('device/reportTemp/<int:device_id>/', views.ReportTemp, name="temp report"),
]
