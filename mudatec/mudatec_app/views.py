from rest_framework import generics
from django.contrib.auth.models import User
from .models import Address, Company
from .serializers import (
  # Address
  AddressSerializer,
  AddressListSerializer,
)

# Create your views here.
class CreateAddressAPIView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ListAddressAPIView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
