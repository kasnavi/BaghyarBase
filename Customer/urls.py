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
    path('api/d/<int:land_id>/check/<int:land_program_id>/', views.check_land),
    path('api/d/<int:land_id>/eo>/', views.expected_output),
    path('api/d/<int:land_id>/new-sch/<int:land_program_id>/', views.ask_schedule),
    path('api/d/<int:device_id>/', views.get_device_serial),
    path('api/', include(router.urls)),
    # path('device/reportTemp/<int:device_id>/', views.reportTemp, name="temp report"),
]
