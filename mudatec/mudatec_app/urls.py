from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import (
  #Address
  CreateAddressAPIView,
  ListAddressAPIView,
  RetrieveAddressAPIView,
  #Company
  ListCompanyAPIView,
  RetrieveCompanyAddressAPIView,
  CreateCompanyAddressAPIView,
  UpdateCompanyAddressAPIView,
  RetrieveUpdateCompanyAPIView,
  RetrieveUpdateCompanyAddressAPIView,
)
0
urlpatterns = [
  path("address/", ListAddressAPIView.as_view(), name="list_address"),
  path("address/create/", CreateAddressAPIView.as_view(), name="create_address"),
  path("address/<int:pk>/", RetrieveAddressAPIView.as_view(), name="retrieve_address"),
  path("company/", ListCompanyAPIView.as_view(), name="list_company"),
  path("company/create/", CreateCompanyAddressAPIView.as_view(), name="create_company"),
  path("company/<int:pk>/", RetrieveCompanyAddressAPIView.as_view(), name="retrieve_company"),
  path("company/<int:pk>/update/", UpdateCompanyAddressAPIView.as_view(), name="update_company"),
  path("company/<int:pk>/patch/", RetrieveUpdateCompanyAPIView.as_view(), name="patch_company"),
  path("company/<int:pk>/patch-address/", RetrieveUpdateCompanyAddressAPIView.as_view(), name="patch_company-address"),
]
