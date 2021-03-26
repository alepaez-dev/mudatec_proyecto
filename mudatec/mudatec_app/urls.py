from django.urls import path
from .views import home, usuario_iniciar_sesion

urlpatterns = [
    path("", home),
    path("iniciar_sesion/", usuario_iniciar_sesion),
]