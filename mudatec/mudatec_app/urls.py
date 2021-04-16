from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views 
from rest_framework.routers import DefaultRouter


from .views import (
  #Address
  CreateAddressAPIView,
  ListAddressAPIView,
  RetrieveAddressAPIView,
  DestroyAddressAPIView,
  UpdateAddressAPIView,

  #Company
  ListCompanyAPIView,
  DestroyCompanyAPIView,
  RetrieveCompanyAddressAPIView,
  CreateCompanyAPIView,
  CreateCompanyAddressAPIView,
  UpdateCompanyAddressAPIView,
  RetrieveUpdateCompanyAPIView,
  RetrieveUpdateCompanyAddressAPIView,
  ListCompanyAddressAPIView,

  #User
  CreateUserAPIView,
  ListUserAPIView,
  UpdateUserAPIView,
  RetrieveUserAPIView,
  DestroyUserAPIView,
  RetrieveUserWithUsernameAPIView,

  #User-Company
  CreateUserCompanyAPIView,
  RetrieveUserFilterIsCompanyAPIView,
  RetrieveUserCompanyAPIView,
  UpdateUserCompanyAPIView,
  DestroyUserCompanyAPIView,
  

  #Post
  CreatePostAPIView,
  ListPostAPIView,
  CreatePostAddressAPIView,
  RetrievePostAddressAPIView,
  UpdatePostAddressAPIView,

  #Token
  ListTokenUserAPIView,
  RetrieveTokenUserAPIView,
  RetrieveTokenUserCompanyAPIView,
)

urlpatterns = [
  #Address
  path("address/", ListAddressAPIView.as_view(), name="list_address"),
  path("address/create/", CreateAddressAPIView.as_view(), name="create_address"),
  path("address/<int:pk>/", RetrieveAddressAPIView.as_view(), name="retrieve_address"),
  path("address/<int:pk>/update/", UpdateAddressAPIView.as_view(), name="update_address"),
  path("address/<int:pk>/destroy/", DestroyAddressAPIView.as_view(), name="destroy_address"),
  #Company
  path("company/", ListCompanyAPIView.as_view(), name="list_company"),
  path("company-address/", ListCompanyAddressAPIView.as_view(), name="list_company_address"),
  path("company/create/", CreateCompanyAPIView.as_view(), name="create_company"),
  # path("company/create-company/", CreateCompanyAddressAPIView.as_view(), name="create_company_address"),
  path("company/<int:pk>/", RetrieveCompanyAddressAPIView.as_view(), name="retrieve_company"),
  path("company/<int:pk>/destroy/", DestroyCompanyAPIView.as_view(), name="destroy_company"),
  path("company/<int:pk>/update/", UpdateCompanyAddressAPIView.as_view(), name="update_company"),
  path("company/<int:pk>/patch/", RetrieveUpdateCompanyAPIView.as_view(), name="patch_company"),
  path("company/<int:pk>/patch-address/", RetrieveUpdateCompanyAddressAPIView.as_view(), name="patch_company-address"),
  #User
  path("user/", ListUserAPIView.as_view(), name="list_user"),
  path("user/login/", views.obtain_auth_token, name="login_users"),
  path("user/create/", CreateUserAPIView.as_view(), name="create_user"),
  path("user/<int:pk>/", RetrieveUserAPIView.as_view(), name="retrieve_user-username"),
  path("user/<int:pk>/update/", UpdateUserAPIView.as_view(), name="update_user"),
  path("user/<int:pk>/destroy/", DestroyUserAPIView.as_view(), name="destroy_user"),
  #User-Company
  path("user/company/create/", CreateUserCompanyAPIView.as_view(), name="create_user_company"),
  path("user/company/<int:pk>/", RetrieveUserCompanyAPIView.as_view(), name="retrieve_user-company"),
  path("user/is_company=<str:pk>/",RetrieveUserFilterIsCompanyAPIView.as_view(), name="retrieve_users_with_company"),
  path("user/company/<int:pk>/update/", UpdateUserCompanyAPIView.as_view(), name="update_user-company"),
  path("user/company/<int:pk>/destroy/", DestroyUserCompanyAPIView.as_view(), name="destroy_user-company"),
  #Post
  path("post/", ListPostAPIView.as_view(), name="list_post"),
  path("post/<int:pk>/", RetrievePostAddressAPIView.as_view(), name="retrieve_post"),
  path("post/<int:pk>/update/", UpdatePostAddressAPIView.as_view(), name="update_post"),
  path("post/create/", RetrievePostAddressAPIView.as_view(), name="create_post"),
  path("post/create-address/", CreatePostAddressAPIView.as_view(), name="create_post_address"),
  # Token
  path("token/", ListTokenUserAPIView.as_view(), name="list_token_user"),
  path("token/<str:pk>/", RetrieveTokenUserAPIView.as_view(), name="retrieve_token_user"),
  path("token/company/<str:pk>/", RetrieveTokenUserCompanyAPIView.as_view(), name="retrieve_token_user_company"),
  ]