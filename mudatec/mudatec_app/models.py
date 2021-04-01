from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Address(models.Model):
    """Direccion."""

    street = models.CharField(max_length=50)
    num_int = models.CharField(max_length=10)
    num_ext = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    references = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __Estr__(self):
        return f"{self.street} {self.address} {self.zip_code}"


class Company(models.Model):
    """Empresas."""

    name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    rfc = models.CharField(max_length=13)
    social_name = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    phone = models.CharField(max_length=15)
    phone = models.DateTimeField(auto_now_add=True)

    #Relations
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="companies")

    def __str__(self):
        return f"{self.name} {self.email}"

class CustomUser(AbstractUser):
    """Usuarios."""

    #Aditional Fields
    mother_last_name = models.CharField(max_length=50)
    is_company = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True)
    payment_id = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True, related_name="customusers")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

class Post(models.Model):
    """Posts"""

    title = models.CharField(max_length=50)

    STATUS_TYPES = (
        ("no_demand", "No_demand"),
        ("in_demand", "In_demand"),
        ("complete", "Complete"),
    )
    status = models.CharField(max_length=50,choices=STATUS_TYPES, default="sin_cotizar")
    dates = ArrayField(ArrayField(models.DateTimeField(max_length=20)))
    edited = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mother_last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60, unique=True)
    phone = models.CharField(max_length=15)
    date_edited = models.DateTimeField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    initial_address = models.ForeignKey(Direccion, on_delete=models.PROTECT, related_name="initial_posts")
    ending_address = models.ForeignKey(Direccion, on_delete=models.PROTECT, related_name="ending_posts")

    def __str__(self):
    return f"{self.title} {self.status}"

class Forms(models.Model):
    """Formularios"""

    furniture = models.CharField(max_length=50)
    quantity = models.IntegerField(blank=True)
    size = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)


    #Relations
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="forms")
    
    def __str__(self):
        return f"{self.furniture} {self.quantity} {self.size}"

class Budget(models.Model):
    """Cotizaciones"""

    STATUS_TYPES = (
    ("pending", "Pending"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
    )
    status = models.CharField(max_length=50, choices=STATUS_TYPES)
    available_dates = ArrayField(ArrayField(models.DateTimeField(max_length=20)))
    agreed_date = models.DateTimeField(blank= True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, min_value=0)
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="budgets")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="budgets")
        
    def __str__(self):
        return f"{self.status} {self.available_dates} {self.amount}"

class Review(models.Model):
    """Reviews"""

    score = models.IntegerField(max_digits=1, min_value=1)
    description_company = models.TextField()
    description_mudatec = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    customUser = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="reviews") 
    budget = models.ForeignKey(Budget, on_delete=models.PROTECT, related_name="reviews")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="reviews")

    def __str__(self):
    return f"{self.score} {self.date_created}"


class Transaction(models.Model):
    """Transacciones"""

    amount = models.DecimalField(max_digits=8, decimal_places=2, min_value=0)
    STATUS_TYPES = (
    ("pending", "Pending"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
    ("completed", "Completed"),
    )
    date_created = models.DateTimeField(auto_now_add=True)

    #Relations
    customUser = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="transactions")
    budget = models.ForeignKey(Budget, on_delete=models.PROTECT, related_name="transactions")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="transactions")

