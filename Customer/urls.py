from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('customer', views.CustomerView)
router.register('user', views.UserViewSet)
router.register('land', views.LandView)

urlpatterns = [
    path('', include(router.urls))
]
