from django.urls import path
from .views import (
  Home, 
  UsuarioRegistro, 
  UsuarioIniciarSesion,
  MudanzaRegistro,
  MudanzaIniciarSesion,
  PerfilUsuario,
  PerfilUsuarioInfo,
  PerfilUsuarioPost,
)

urlpatterns = [
    path("", Home),
    path("usuario/registro/", UsuarioRegistro),
    path("usuario/iniciar_sesion/", UsuarioIniciarSesion),
    path("mudanza/registro/", MudanzaRegistro),
    path("mudanza/iniciar_sesion/", MudanzaIniciarSesion),
    path("usuario/perfil/", PerfilUsuario),
    path("usuario/perfil/info/", PerfilUsuarioInfo),
    path("usuario/perfil/post/", PerfilUsuarioPost),
]