from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Home(request):
    """Landing Page."""
    context = {}
    template = loader.get_template("mudatec_app/index.html")
    return HttpResponse(template.render(context,request))

def UsuarioRegistro(request):
    """Landing Page."""
    context = {}
    template = loader.get_template("mudatec_app/usuario/registro.html")
    return HttpResponse(template.render(context,request))

def UsuarioIniciarSesion(request):
    """Landing Page."""
    context = {}
    template = loader.get_template("mudatec_app/usuario/iniciar_sesion.html")
    return HttpResponse(template.render(context,request))

