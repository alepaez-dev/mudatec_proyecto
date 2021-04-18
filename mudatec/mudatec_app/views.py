from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import(
  Address,
  Company, 
  CustomUser,
  Post,
  Form,
  Budget,
)
from rest_framework import viewsets

from .serializers import (
  # Address
  AddressSerializer,
  AddressListSerializer,
  CompanyForAddressSerializer,
  #Company
  CompanySerializer,
  CompanyListSerializer,
  CompanyAddressSerializer,
  #User
  CustomUserSerializer,
  CustomUserReadSerializer,
  CustomUserPassSerializer,
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
  TokenUserCompanySerializer,
  #Budget
  BudgetSerializer,
)

# Create your views here.

# ADDRESS
class ListAddressAPIView(generics.ListAPIView):
  queryset = Address.objects.all()
  serializer_class = AddressListSerializer

class CreateAddressAPIView(generics.CreateAPIView):
  queryset = Address.objects.all()
  serializer_class = AddressSerializer

class UpdateAddressAPIView(generics.UpdateAPIView):
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
class ListCompanyAddressAPIView(generics.ListAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanyAddressSerializer

class CreateCompanyAddressAPIView(generics.CreateAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanyAddressSerializer

class RetrieveCompanyAddressAPIView(generics.RetrieveAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanyAddressSerializer

class UpdateCompanyAddressAPIView(generics.UpdateAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanyForAddressSerializer

class RetrieveUpdateCompanyAPIView(generics.RetrieveUpdateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Company.objects.all()
  serializer_class = CompanySerializer

class RetrieveUpdateCompanyAddressAPIView(generics.RetrieveUpdateAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanyAddressSerializer

#USER
class ListUserAPIView(generics.ListAPIView):
  queryset = CustomUser.objects.all().order_by("date_created").reverse()
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


class UpdateUserAPIView(generics.RetrieveUpdateAPIView):
  # permission_classes = [IsAuthenticated]
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer

class UpdateUserPassAPIView(generics.RetrieveUpdateAPIView):
  # permission_classes = [IsAuthenticated]
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserPassSerializer

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
    return CustomUser.objects.filter(is_company=is_company).order_by("date_created").reverse()

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
class ListPostAddressAPIView(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostAddressSerializer

class CreatePostAddressAPIView(generics.CreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostAddressSerializer

class RetrievePostAddressAPIView(generics.RetrieveAPIView):
  serializer_class = PostAddressSerializer
  queryset = Post.objects.all()

class UpdatePostAddressAPIView(generics.RetrieveUpdateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostAddressSerializer

class RetrievePostAddressUserAPIView(generics.ListAPIView):
  serializer_class = PostAddressSerializer

  def get_queryset(self):
    """Filtering with the URL"""
    customuser = self.kwargs["pk"]
    return Post.objects.filter(customuser=customuser).order_by("date_created").reverse()

#Form
class CreateFormAPIView(generics.CreateAPIView):
  queryset = Form.objects.all()
  serializer_class = FormSerializer

class ListFormAPIView(generics.ListAPIView):
  queryset = Form.objects.all()
  serializer_class = FormSerializer

class UpdateFormAPIView(generics.UpdateAPIView):
  queryset = Form.objects.all()
  serializer_class = FormSerializer

class DestroyFormAPIView(generics.DestroyAPIView):
  queryset = Form.objects.all()
  serializer_class = FormSerializer

#Token 
class ListTokenUserAPIView(generics.ListAPIView):
  # permission_classes = [IsAuthenticated]
  queryset = Token.objects.all()
  serializer_class = TokenUserSerializer

class RetrieveTokenUserAPIView(generics.RetrieveAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Token.objects.all()
  serializer_class = TokenUserSerializer

class RetrieveTokenUserCompanyAPIView(generics.RetrieveAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Token.objects.all()
  serializer_class = TokenUserCompanySerializer

# Budget
class CreateBudgetAPIView(generics.CreateAPIView):
  queryset = Budget.objects.all()
  serializer_class = BudgetSerializer

class ListBudgetAPIView(generics.ListAPIView):
  queryset = Budget.objects.all()
  serializer_class = BudgetSerializer

class RetrieveBudgetCompanyAPIView(generics.ListAPIView):
  serializer_class = BudgetSerializer

  def get_queryset(self):
    """Filtering with the URL"""
    company = self.kwargs["pk"]
    return Budget.objects.filter(company=company).order_by("date_created").reverse()

class RetrieveBudgetPostAPIView(generics.ListAPIView):
  serializer_class = BudgetSerializer

  def get_queryset(self):
    """Filtering with the URL"""
    post = self.kwargs["pk"]
    return Budget.objects.filter(post=post).order_by("date_created").reverse()