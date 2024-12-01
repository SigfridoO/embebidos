from django.shortcuts import render
from .models import Memoria

def home(request):
    memorias = Memoria.objects.all()
    return render(request, "core/index.html", {'memorias': memorias})

def cocos(request):
    return render(request, "core/cocos.html")

def domotica(request):
    return render(request, "core/domotica.html")

def empaquetadora(request):
    return render(request, "core/empaquetadora.html")

def hidroponia(request):
    return render(request, "core/hidroponia.html")

def riego(request):
    return render(request, "core/riego.html")

def mapa(request):
    return render(request, "core/mapa.html")