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
  #User
  CreateUserAPIView,
  ListUserAPIView,
  UpdateUserAPIView,
  RetrieveAddressAPIView,
)

urlpatterns = [
  #Address
  path("address/", ListAddressAPIView.as_view(), name="list_address"),
  path("address/create/", CreateAddressAPIView.as_view(), name="create_address"),
  path("address/<int:pk>/", RetrieveAddressAPIView.as_view(), name="retrieve_address"),
  #Company
  path("company/", ListCompanyAPIView.as_view(), name="list_company"),
  path("company/create/", CreateCompanyAddressAPIView.as_view(), name="create_company"),
  path("company/<int:pk>/", RetrieveCompanyAddressAPIView.as_view(), name="retrieve_company"),
  path("company/<int:pk>/update/", UpdateCompanyAddressAPIView.as_view(), name="update_company"),
  path("company/<int:pk>/patch/", RetrieveUpdateCompanyAPIView.as_view(), name="patch_company"),
  path("company/<int:pk>/patch-address/", RetrieveUpdateCompanyAddressAPIView.as_view(), name="patch_company-address"),
  #User
  path("user/", ListUserAPIView.as_view(), name="list_user"),
  path("user/create/", CreateUserAPIView.as_view(), name="create_user"),
  path("user/<int:pk>/", RetrieveAddressAPIView.as_view(), name="retrieve_user"),
  path("user/<int:pk>/update/", UpdateUserAPIView.as_view(), name="update_user"),]
