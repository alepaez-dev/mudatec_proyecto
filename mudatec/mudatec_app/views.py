from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest
from django.http import JsonResponse
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .serializers import StatusEngSpa
from dotenv import load_dotenv
load_dotenv()
SECRET_SENDGRID_API_KEY = os.getenv("SECRET_SENDGRID_API_KEY")



import sys, json

from .models import(
  Address,
  Company, 
  CustomUser,
  Post,
  Form,
  Budget,
  Transaction,
  # Producto,
  # Compra,
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
  PostUpdateSerializer,
  PostUpdateDatesSerializer,
  #Post-Address,
  PostAddressSerializer,
  #Form
  FormSerializer,
  #Token
  TokenUserSerializer,
  TokenUserCompanySerializer,
  #Budget
  BudgetSerializer,
  BudgetUpdateSerializer,
  #Transaction
  TransactionSerializer,
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

class DestroyNormalUserAPIView(generics.DestroyAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer


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

class UpdatePostAPIView(generics.UpdateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostUpdateSerializer

class UpdatePostDatesAPIView(generics.UpdateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostUpdateDatesSerializer

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
  permission_classes = [IsAuthenticated]
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

class UpdateBudgetAPIView(generics.UpdateAPIView):
  queryset = Budget.objects.all()
  serializer_class = BudgetUpdateSerializer

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
    return Budget.objects.filter(post=post).order_by('status')

#Transaction

class ListTransactionAPIView(generics.ListAPIView):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer

class CreateTransactionAPIView(generics.CreateAPIView):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer

def pago(request):
  # Correo y template para correos
  TEMPLATE_ID_SEND_PAYMENT = "d-863d6064f71945939310d0626055eff7"
  TEMPLATE_ID_RECEIVE_PAYMENT = "d-2a0773aaab0348018729952f7287697a"
  FROM_EMAIL = 'mudatecale@gmail.com'
  
  data = json.loads(request.body)
  id_cotizacion = data['budget_id']
  amount = data['amount']
  order_id = data['orderID']
  budget = Budget.objects.get(id=id_cotizacion)
  
  detalle = GetOrder().get_order(order_id)
  detalle_precio = float(detalle.result.purchase_units[0].amount.value)

  if detalle_precio == float(budget.amount):
    trx = CaptureOrder().capture_order(order_id, debug=True)
    pedido = Transaction.objects.create(
      # pk = trx.result.id,
      estado = trx.result.status,
      amount = float(budget.amount),
      paypal_order = trx.result.id,
      customuser = budget.post.customuser,
      company = budget.company,
      budget = budget,
      total_de_la_compra = trx.result.purchase_units[0].payments.captures[0].amount.value,
      nombre_cliente = trx.result.payer.name.given_name,
      apellido_cliente = trx.result.payer.name.surname,
      correo_cliente =  trx.result.payer.email_address,
      direccion_cliente = trx.result.purchase_units[0].shipping.address.address_line_1)
    pedido.save()

    # Mandamos correo a cliente
    email_payer = budget.post.customuser.email
    if(email_payer != ""):
      message = Mail(
        from_email=FROM_EMAIL,
        to_emails= email_payer,
        subject='Notificacion Mudatec')
      message.dynamic_template_data = {
      'subject': 'Notificacion Mudatec',
      'receiver_name': budget.post.customuser.first_name,
      'payer_name' : budget.company.name,
      'amount' : detalle_precio
      }
      message.template_id = TEMPLATE_ID_SEND_PAYMENT
      try:
        sg = SendGridAPIClient(SECRET_SENDGRID_API_KEY)
        response = sg.send(message)
        print("EMAIL PAYER: ", email_payer)
        print(response.status_code)
        print(response.body)
        print(response.headers)
      except Exception as e:
        print(e.message)

    # Mandamos correo a la empresa
    email_company = budget.company.email
    if(email_company != ""):
      message = Mail(
        from_email=FROM_EMAIL,
        to_emails= email_company,
        subject='Notificacion Mudatec')
      message.dynamic_template_data = {
      'subject': 'Notificacion Mudatec',
      'receiver_name': budget.company.name,
      'amount' : detalle_precio
      }
      message.template_id = TEMPLATE_ID_RECEIVE_PAYMENT
      try:
        sg = SendGridAPIClient(SECRET_SENDGRID_API_KEY)
        response = sg.send(message)
        print("EMAIL PAYER: ", email_payer)
        print(response.status_code)
        print(response.body)
        print(response.headers)
      except Exception as e:
        print(e.message)

    data = {
      "id": f"{trx.result.id}",
      "nombre_cliente": f"{trx.result.payer.name.given_name}",
      "mensaje": "Transacción exitosa",
      "completed": True,
      "recepter_email": email_payer,
      "company": budget.company.name,
      "amount": detalle_precio,
    }
    return JsonResponse(data)
  else:
    data = {
      "mensaje": "No son los precios correctos =(",
      "completed": False
    }
    return JsonResponse(data)



class PayPalClient:
  def __init__(self):
    self.client_id = "AeZnxY0DfNCWw-GJK2_-8BE1Hk79OIRzPe4aS9-m-M7PcbuVQ2ptpximOftX8ed9yhqMuOPfZs7Qo9Yh"
    self.client_secret = "ECfqrPD156xvvmBTmXdSshGVOEtpN9Fry0G969lwf-Nd7TPPjVaUcBbS5YtEoB6YIMrLd54iaRxRoWh8"

    """Set up and return PayPal Python SDK environment with PayPal access credentials.
      This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

    self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)

    """ Returns PayPal HTTP client instance with environment that has access
      credentials context. Use this instance to invoke PayPal APIs, provided the
      credentials have access. """
    self.client = PayPalHttpClient(self.environment)

  def object_to_json(self, json_data):
    """
    Function to print all json data in an organized readable manner
    """
    result = {}
    if sys.version_info[0] < 3:
      itr = json_data.__dict__.iteritems()
    else:
      itr = json_data.__dict__.items()
      for key,value in itr:
        # Skip internal attributes.
        if key.startswith("__"):
          continue
        result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
        self.object_to_json(value) if not self.is_primittive(value) else\
        value
      return result
  def array_to_json_array(self, json_array):
    result =[]
    if isinstance(json_array, list):
      for item in json_array:
        result.append(self.object_to_json(item) if  not self.is_primittive(item) \
            else self.array_to_json_array(item) if isinstance(item, list) else item)
    return result

  def is_primittive(self, data):
    return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)


##Obtener los detalles de la transaccion
class GetOrder(PayPalClient):

  #2. Set up your server to receive a call from the client
  """You can use this function to retrieve an order by passing order ID as an argument"""   
  def get_order(self, order_id):
    """Method to get order"""
    request = OrdersGetRequest(order_id)
    #3. Call PayPal to get the transaction
    response = self.client.execute(request)
    return response



##Capturar la order
class CaptureOrder(PayPalClient):

  #2. Set up your server to receive a call from the client
  """this sample function performs payment capture on the order.
  Approved order ID should be passed as an argument to this function"""

  def capture_order(self, order_id, debug=False):
    """Method to capture order using order_id"""
    request = OrdersCaptureRequest(order_id)
    #3. Call PayPal to capture an order
    response = self.client.execute(request)
    #4. Save the capture ID to your database. Implement logic to save capture to your database for future reference.
    if debug:
      print('Status Code: ', response.status_code)
      print('Status: ', response.result.status)
      print('Order ID: ', response.result.id)
      print('Links: ')
      for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
      print('Capture Ids: ')
      for purchase_unit in response.result.purchase_units:
        for capture in purchase_unit.payments.captures:
          print('\t', capture.id)
      print("Buyer:")
     
    return response


"""This driver function invokes the capture order function.
Replace Order ID value with the approved order ID. """
