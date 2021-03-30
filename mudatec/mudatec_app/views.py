from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Home(request):
    """Landing Page."""
    context = {}
    template = loader.get_template("mudatec_app/index.html")
    return HttpResponse(template.render(context,request))

#Usuarios
def UsuarioRegistro(request):
    """Usuario Registro"""
    context = {}
    template = loader.get_template("mudatec_app/usuario/registro.html")
    return HttpResponse(template.render(context,request))

def UsuarioIniciarSesion(request):
    """Usuario Iniciar Sesion."""
    context = {}
    template = loader.get_template("mudatec_app/usuario/iniciar_sesion.html")
    return HttpResponse(template.render(context,request))

#Usuarios perfiles
def PerfilUsuario(request):
    """Perfil Usuario"""
    context = {}
    template = loader.get_template("perfil.html")
    return HttpResponse(template.render(context,request))

def PerfilUsuarioInfo(request):
    """Perfil Usuario Info"""
    context = {}
    template = loader.get_template("mudatec_app/usuario/info.html")
    return HttpResponse(template.render(context,request))

def PerfilUsuarioPost(request):
    """Perfil Usuario Info"""
    context = {}
    template = loader.get_template("mudatec_app/usuario/post.html")
    return HttpResponse(template.render(context,request))

#Mudanza
def MudanzaRegistro(request):
    """Mudanza Registro."""
    context = {}
    template = loader.get_template("mudatec_app/mudanza/registro.html")
    return HttpResponse(template.render(context,request))

def MudanzaIniciarSesion(request):
    """Mudanza Iniciar Sesion."""
    context = {}
    template = loader.get_template("mudatec_app/mudanza/iniciar_sesion.html")
    return HttpResponse(template.render(context,request))


  

