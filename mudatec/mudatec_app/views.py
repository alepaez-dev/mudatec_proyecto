from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import(
  Address,
  Company, 
  CustomUser,
  Post,
  Form,
)
from rest_framework import viewsets

from .serializers import (
  # Address
  AddressSerializer,
  AddressListSerializer,
  #Company
  CompanySerializer,
  CompanyListSerializer,
  CompanyAddressSerializer,
  #User
  CustomUserSerializer,
  CustomUserReadSerializer,
  #User-Company
  CustomUserCompanySerializer,
  CustomUserCompanyReadSerializer,
  #Post
  PostSerializer,
  #Post-Address,
  PostAddressSerializer,
  #Form
  FormSerializer,
  # Token
  TokenUserSerializer,
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

class DestroyAddressAPIView(generics.DestroyAPIView):
  queryset = Address.objects.all()
  serializer_class = AddressSerializer

#COMPANY
class ListCompanyAPIView(generics.ListAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanyListSerializer

class CreateCompanyAPIView(generics.CreateAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer

class DestroyCompanyAPIView(generics.DestroyAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer


#COMPANY-ADDRESS
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
  serializer_class = CompanyAddressSerializer

#USER
class ListUserAPIView(generics.ListAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserReadSerializer

class CreateUserAPIView(generics.CreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer

class RetrieveUserAPIView(generics.RetrieveAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserReadSerializer

class RetrieveUserWithUsernameAPIView(generics.ListAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserReadSerializer
  def get_queryset(self):
    """Filtering with the URL"""
    username = self.kwargs["pk"]
    return CustomUser.objects.filter(username=username)

class UpdateUserAPIView(generics.RetrieveUpdateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer

class DestroyUserAPIView(generics.DestroyAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserCompanySerializer


#USER-COMPANY
class CreateUserCompanyAPIView(generics.CreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserCompanySerializer

class RetrieveUserCompanyAPIView(generics.RetrieveAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserCompanyReadSerializer

class RetrieveUserFilterIsCompanyAPIView(generics.ListAPIView):
  serializer_class = CustomUserCompanyReadSerializer

  def get_queryset(self):
    """Filtering with the URL"""
    is_company = self.kwargs["pk"]
    return CustomUser.objects.filter(is_company=is_company)

class UpdateUserCompanyAPIView(generics.RetrieveUpdateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserCompanySerializer
    
class DestroyUserCompanyAPIView(generics.DestroyAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserCompanySerializer

#POST
class CreatePostAPIView(generics.CreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class ListPostAPIView(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

#POST-ADDRESS
class CreatePostAddressAPIView(generics.CreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostAddressSerializer

class RetrievePostAddressAPIView(generics.RetrieveAPIView):
  serializer_class = PostAddressSerializer
  queryset = Post.objects.all()

class UpdatePostAddressAPIView(generics.RetrieveUpdateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostAddressSerializer

#Form
class CreateFormAPIView(generics.CreateAPIView):
  queryset = Form.objects.all()
  serializer_class = FormSerializer

class ListFormAPIView(generics.ListAPIView):
  queryset = Form.objects.all()
  serializer_class = FormSerializer

# 

class ListTokenUserAPIView(generics.ListAPIView):
  queryset = Token.objects.all()
  serializer_class = TokenUserSerializer

class RetrievePostAddressAPIView(generics.RetrieveAPIView):
  queryset = Token.objects.all()
  serializer_class = TokenUserSerializer
