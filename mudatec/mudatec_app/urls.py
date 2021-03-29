from django.urls import path
from .views import (
  Home, 
  UsuarioRegistro, 
  UsuarioIniciarSesion,
  MudanzaRegistro,
  MudanzaIniciarSesion,
  PerfilUsuario,
)

urlpatterns = [
    path("", Home),
    path("usuario/registro", UsuarioRegistro),
    path("usuario/iniciar_sesion", UsuarioIniciarSesion),
    path("mudanza/registro", MudanzaRegistro),
    path("mudanza/iniciar_sesion", MudanzaIniciarSesion),
    path("usuario/perfil", PerfilUsuario),
]