from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import (
  Address, 
  Company,
  CustomUser,
  Post,
  Form,
  Budget,
)
  

# Serializers define the API representation.

#Address
class AddressSerializer(serializers.ModelSerializer):
  """Address"""
  class Meta:
    model = Address
    fields = [
      "id",
      "street",
      "num_int",
      "num_ext",
      "address",
      "zip_code",
      "references",
      "floor",
      "stairs",
      "elevator",
      "rope_flow",
    ]
  

class AddressListSerializer(serializers.ModelSerializer):
  """Address List"""
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
  """Company"""
  class Meta:
    model = Company
    fields = "__all__"

class CompanyListSerializer(serializers.ModelSerializer):
  """Company List"""
  class Meta:
    model = Company
    fields = [
      "id", 
      "name",
      "email",
    ]

class CompanyAddressSerializer(serializers.ModelSerializer):
  """Company y Address"""
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
    
class CompanyForAddressSerializer(serializers.ModelSerializer):
  """Company y Address"""
  address = AddressSerializer()
  class Meta:
    model = Company
    fields = [
      "id",
      "address",
    ]
  def update(self, instance, validated_data):
    pam = validated_data.pop("address")
    compas = Company.objects.get(id=instance.id)
    address = Address.objects.create(**pam)
    compas.address = address
    compas.save()
    return compas


#CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
  """User"""
  
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
        "id",
      ]
      
  def create(self, validated_data):
    customuser = super(CustomUserSerializer, self).create(validated_data)
    customuser.set_password(validated_data['password'])
    Token.objects.create(user=customuser)
    customuser.save()
    return customuser
  
  def update(self, instance, validated_data):
    customuser = super(CustomUserSerializer, self).update(instance, validated_data)
    # customuser.set_password(validated_data['password'])
    # customuser.save()
    customuser.save()
    return customuser

class CustomUserPassSerializer(serializers.ModelSerializer):
  """User"""
  
  class Meta:
      model = CustomUser
      fields = [
        "username",
        "id",
        "password",
      ]
      
  def update(self, instance, validated_data):
    customuser = super(CustomUserPassSerializer, self).update(instance, validated_data)
    print("aaaaaaaa",customuser)
    token1 = Token.objects.get(user=customuser)
    print("token11111111", token1)
    Token.objects.get(user=customuser).delete()
    customuser.set_password(validated_data['password'])
    customuser.save()
    print(customuser.password)
    token2 = Token.objects.create(user=customuser)
    customuser.save()
    print("token22222222", token2)
    return customuser

class CustomUserCompanyReadSerializer(serializers.ModelSerializer):
  """User con Company y Address para ver"""
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

class CustomUserCompanyAddressSerializer(serializers.ModelSerializer):
  """User con Company y Address"""
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
    Token.objects.create(user=customuser)
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

class CustomUserCompanySerializer(serializers.ModelSerializer):
  """User con Company y Address"""
  company = CompanySerializer()
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
        "id",
      ]
      
  def create(self, validated_data):
    company_id = self.validated_data.pop("company")
    company = Company.objects.create(**company_id)
    validated_data.pop("company")
    customuser = CustomUser.objects.create(company=company, **validated_data)
    customuser.set_password(validated_data['password'])
    Token.objects.create(user=customuser)
    customuser.save()
    return customuser

  def update(self, instance, validated_data):
    company_id = self.validated_data.pop("company")
    validated_data.pop("company")
    instance.company = super().update(instance.company, company_id)
    instance = super().update(instance, validated_data)
    customuser = super(CustomUserCompanySerializer, self).update(instance, validated_data)
    customuser.set_password(validated_data["password"])
    customuser.save()
    return customuser

class CustomUserReadSerializer(serializers.ModelSerializer):
  """User solo para ver"""
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
  """Post"""
  class Meta:
    model = Post
    fields = "__all__"

class PostUpdateSerializer(serializers.ModelSerializer):
  """Post"""
  class Meta:
    model = Post
    fields = [
      "name",
      "last_name",
      "mother_last_name",
    ]

class PostUpdateDatesSerializer(serializers.ModelSerializer):
  """Post"""
  class Meta:
    model = Post
    fields = [
      "dates"
    ]

#Form
class FormSerializer(serializers.ModelSerializer):
  """Post"""
  class Meta:
    model = Form
    fields = "__all__"

#Post-Addres
class PostAddressSerializer(serializers.ModelSerializer):
  """Post con Address"""
  #llaves foraneas
  forms = FormSerializer(many=True)
  initial_address = AddressSerializer()
  ending_address = AddressSerializer()

  # date_created = serializers.DateField(format='%m-%d-%y')
  class Meta:
    model = Post
    fields = [
      "id",
      "title",
      "status",
      "dates",
      "edited",
      "name",
      "last_name",
      "mother_last_name",
      "phone",
      "date_edited",
      "customuser",
      "initial_address",
      "ending_address",
      "forms",
      "date_created",
    ]

  def create(self, validated_data):
    initial_address_id = self.validated_data.pop("initial_address")
    ending_address_id = self.validated_data.pop("ending_address")
    forms_id = self.validated_data.pop("forms")
    initial_address = Address.objects.create(**initial_address_id)
    ending_address = Address.objects.create(**ending_address_id)
    array_forms = []
    for form_id in forms_id:
      form = Form.objects.create(**form_id)
      array_forms.append(form)
    validated_data.pop("initial_address")
    validated_data.pop("ending_address")
    validated_data.pop("forms")
    post = Post.objects.create(initial_address=initial_address,ending_address=ending_address, **validated_data)
    post.forms.set(array_forms)
    return post

  def update(self, instance, validated_data):
    initial_address_id = self.validated_data.pop("initial_address")
    ending_address_id = self.validated_data.pop("ending_address")
    forms_id = self.validated_data.pop("forms")
    validated_data.pop("initial_address")
    validated_data.pop("ending_address")
    forms_viejo = list(Form.objects.filter(post_id=instance.id))
    for form in range(len(forms_id)):
      forms_nuevo = super().update(forms_viejo[form], forms_id[form])
    validated_data.pop("forms")
    instance.initial_address = super().update(instance.initial_address, initial_address_id)
    instance.ending_address = super().update(instance.ending_address, ending_address_id)
    instance = super().update(instance, validated_data)
    post = super(PostAddressSerializer, self).update(instance, validated_data)
    post.save()
    return post

#Token
class TokenUserSerializer(serializers.ModelSerializer):
  """Token"""
  user = CustomUserSerializer()

  class Meta:
    model = Token  
    fields = "__all__"

class TokenUserCompanySerializer(serializers.ModelSerializer):
  """Token"""
  user = CustomUserCompanySerializer()

  class Meta:
    model = Token  
    fields = "__all__"

# Budget
class BudgetSerializer(serializers.ModelSerializer):
  """Budget"""
  # post = PostSerializer()
  # company = CompanySerializer()

  class Meta:
    model = Budget
    fields = "__all__"
