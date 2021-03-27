from django.urls import path
from .views import home, usuario_registro

urlpatterns = [
    path("", home),
    path("registro/", usuario_registro),
]