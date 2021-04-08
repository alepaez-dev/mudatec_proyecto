from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Address, Company, CustomUser

# Serializers define the API representation.

#Address
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

#Company
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

    def update(self, instance, validated_data):
      if validated_data.get('address'):
        address_data = validated_data.get('address')
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
          address = address_serializer.update(instance=instance.address,validated_data=address_serializer.validated_data)
          validated_data['address'] = address
      return super().update(instance, validated_data)

#CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
          "username",
          "password",
          "first_name",
          "last_name",
          "mother_last_name",
          "email",
          "is_company",
          "phone",
          "payment_id",
          "company",
        ]
      
    def create(self, validated_data):
      customuser = super(CustomUserSerializer, self).create(validated_data)
      customuser.set_password(validated_data['password'])
      customuser.save()
      return customuser

    def update(self, instance, validated_data):
      instance.set_password(validated_data['password'])
      return instance


class CustomUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
          "username",
          "first_name",
          "last_name",
          "mother_last_name",
          "email",
          "phone",
          "payment_id",
          "company",
          "id",
        ]
