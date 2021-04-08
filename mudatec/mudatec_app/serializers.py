from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address, Company

# Serializers define the API representation.

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
          "street",
          "num_int",
          "num_ext",
          "address",
          "zip_code",
          "references",
        ]

class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
          "id", 
          "street",
          "address",
          "zip_code",
        ]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class CompanyListSerializer(serializers.ModelSerializer):
  #llave foranea

    class Meta:
        model = Company
        fields = [
          "id", 
          "name",
          "email",
        ]

class CompanyAddressSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
      address_id = self.validated_data.pop("address")
      address = Address.objects.create(**address_id)
      validated_data.pop("address");
      company = Company.objects.create(address=address, **validated_data)
      return company




