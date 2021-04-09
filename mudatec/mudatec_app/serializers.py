from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Address, Company, CustomUser, Post

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
        "phone",
        "payment_id",
      ]
      
  def create(self, validated_data):
    customuser = super(CustomUserSerializer, self).create(validated_data)
    customuser.set_password(validated_data['password'])
    customuser.save()
    return customuser
  
  def update(self, instance, validated_data):
    customuser = super(CustomUserSerializer, self).update(instance, validated_data)
    customuser.set_password(validated_data['password'])
    return customuser

class CustomUserCompanyReadSerializer(serializers.ModelSerializer):
  company = CompanyAddressSerializer()
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
        "is_company",
        "company",
      ]

class CustomUserCompanySerializer(serializers.ModelSerializer):
  company = CompanyAddressSerializer()
  class Meta:
      model = CustomUser
      fields = [
        "username",
        "password",
        "first_name",
        "last_name",
        "mother_last_name",
        "email",
        "phone",
        "payment_id",
        "is_company",
        "company",
      ]
      
  def create(self, validated_data):
    company_id = self.validated_data.pop("company")
    address_id = company_id.pop("address")
    address = Address.objects.create(**address_id)
    company = Company.objects.create(address=address, **company_id)
    validated_data.pop("company")
    customuser = CustomUser.objects.create(company=company, **validated_data)
    customuser.set_password(validated_data['password'])
    customuser.save()
    return customuser

  def update(self, instance, validated_data):
    company_id = self.validated_data.pop("company")
    address_id = company_id.pop("address")
    validated_data.pop("company")
    instance.company.address = super().update(instance.company.address, address_id)
    instance.company = super().update(instance.company, company_id)
    instance = super().update(instance, validated_data)
    customuser = super(CustomUserCompanySerializer, self).update(instance, validated_data)
    customuser.set_password(validated_data["password"])
    customuser.save()
    return customuser

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

#Post
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"

class PostAddressSerializer(serializers.ModelSerializer):
  initial_address = AddressSerializer()
  ending_address = AddressSerializer()
  class Meta:
    model = Post
    fields = "__all__"

  def create(self, validated_data):
    initial_address_id = self.validated_data.pop("initial_address")
    ending_address = self.validated_data.pop("ending_address")
    initial_address = Address.objects.create(**initial_address_id)
    ending_address = Address.objects.create(**ending_address)
    validated_data.pop("initial_address");
    validated_data.pop("ending_address");
    post = Post.objects.create(initial_address=initial_address,ending_address=ending_address, **validated_data)
    return post