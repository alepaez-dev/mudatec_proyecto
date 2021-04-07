from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address, Company

# Serializers define the API representation.

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
          "id", 
          "street",
          "address",
          "zip_code",
        ]