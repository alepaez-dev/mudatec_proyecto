from rest_framework import generics
from django.contrib.auth.models import User
from .models import Address, Company
from .serializers import (
  # Address
  AddressSerializer,
  AddressListSerializer,
  #Company
  CompanySerializer,
  CompanyListSerializer,
  CompanyAddressSerializer,
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

