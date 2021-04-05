from django.urls import path
from .views import (
  Home, UsuarioRegistro, UsuarioIniciarSesion
)

urlpatterns = [
    path("", Home),
    path("usuario/registro", UsuarioRegistro),
    path("usuario/iniciar_sesion", UsuarioRegistro),
]