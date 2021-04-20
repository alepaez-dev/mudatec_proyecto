from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Address(models.Model):
    """Direccion."""
    street = models.CharField(max_length=50)
    num_int = models.CharField(max_length=10, blank=True)
    num_ext = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    references = models.TextField(blank = True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street} {self.address} {self.zip_code}"


class Company(models.Model):
    """Empresas."""

    name = models.CharField(max_length=50)
    rfc = models.CharField(max_length=13, blank=True)
    social_name = models.CharField(max_length=60,blank=True)
    email = models.EmailField(max_length=60, blank=True)
    phone = models.CharField(max_length=15,  blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    address = models.ForeignKey(Address, on_delete=models.PROTECT,blank=True, null=True, related_name="companies")

    def __str__(self):
        return f"{self.name}"

class CustomUser(AbstractUser):
    """Usuarios."""

    #Aditional Fields
    mother_last_name = models.CharField(max_length=50,blank=True)
    is_company = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True)
    payment_id = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True, related_name="customuser")
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

class Post(models.Model):
    """Posts"""

    title = models.CharField(max_length=50)

    STATUS_TYPES = (
        ("no_demand", "No Demand"),
        ("in_demand", "In Demand"),
        ("complete", "Complete"),
    )
    status = models.CharField(max_length=50,choices=STATUS_TYPES, default="no_demand")
    dates = ArrayField(ArrayField(models.DateField(max_length=20)))
    edited = models.BooleanField(default=False)
    #User
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mother_last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True)
    date_edited = models.DateField(blank=True, null= True)
    date_created = models.DateField(auto_now_add=True)

    #Relations
    customuser = models.OneToOneField(CustomUser, on_delete=models.PROTECT, related_name="posts", blank=True, null=True)
    initial_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="initial_posts", blank=True, null=True)
    ending_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="ending_posts", blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.status}"

class Form(models.Model):
    """Formularios"""

    furniture = models.CharField(max_length=50)
    quantity = models.IntegerField(blank=True)
    size = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)

    #Relations
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="forms", blank=True, null=True)
    
    def __str__(self):
        return f"{self.furniture} {self.quantity} {self.size}"

class Budget(models.Model):
    """Cotizaciones"""

    STATUS_TYPES = (
    ("pending", "Pending"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
    )
    status = models.CharField(max_length=50, choices=STATUS_TYPES, default="pending")
    # available_dates = ArrayField(ArrayField(models.DateTimeField(max_length=20)))
    agreed_date = models.DateTimeField(blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="budgets")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="budgets")
        
    def __str__(self):
        return f"{self.status} {self.available_dates} {self.amount}"

class Review(models.Model):
    """Reviews"""

    score = models.IntegerField()
    description_company = models.TextField()
    description_mudatec = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    customuser = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="reviews") 
    budget = models.ForeignKey(Budget, on_delete=models.PROTECT, related_name="reviews")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="reviews")

    def __str__(self):
        return f"{self.score} {self.date_created}"


class Transaction(models.Model):
    """Transacciones"""

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    STATUS_TYPES = (
    ("pending", "Pending"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
    ("completed", "Completed"),
    )
    status = models.CharField(max_length=50, choices=STATUS_TYPES, default="pending")
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    customuser = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="transactions")
    budget = models.ForeignKey(Budget, on_delete=models.PROTECT, related_name="transactions")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="transactions")

    def __str__(self):
        return f"{self.amount} {self.status} {self.date_created}"
