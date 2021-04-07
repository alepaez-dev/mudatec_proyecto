from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views 

from .views import (
  #Address
  CreateAddressAPIView,
  ListAddressAPIView
)

urlpatterns = [
  path("address/", ListAddressAPIView.as_view(), name="list_address"),
  path("address/create/", CreateAddressAPIView.as_view(), name="create_address"),
]
