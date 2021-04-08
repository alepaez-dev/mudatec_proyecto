from rest_framework import generics
from django.contrib.auth.models import User
from .models import Address, Company
from rest_framework import viewsets

from .serializers import (
  # Address
  AddressSerializer,
  AddressListSerializer,
  #Company
  CompanySerializer,
  CompanyListSerializer,
  CompanyAddressSerializer,
  CompanyAddressSerializer_2,
)

# Create your views here.

# ADDRESS
class ListAddressAPIView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer

class CreateAddressAPIView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class RetrieveAddressAPIView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

#COMPANY
class ListCompanyAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer

class CreateCompanyAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CreateCompanyAddressAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyAddressSerializer

class RetrieveCompanyAddressAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyAddressSerializer

class UpdateCompanyAddressAPIView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyAddressSerializer

class RetrieveUpdateCompanyAPIView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class RetrieveUpdateCompanyAddressAPIView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyAddressSerializer_2