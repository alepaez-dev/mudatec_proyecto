from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    """Landing Page."""
    context = {}
    template = loader.get_template("mudatec_app/index.html")
    return HttpResponse(template.render(context,request))

def usuario_iniciar_sesion(request):
    """Landing Page."""
    context = {}
    template = loader.get_template("mudatec_app/usuario/iniciar_sesion.html")
    return HttpResponse(template.render(context,request))

