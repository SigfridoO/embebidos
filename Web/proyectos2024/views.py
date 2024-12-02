from django.shortcuts import render
from .models import Memoria

def home(request):
    memorias = Memoria.objects.all()
    return render(request, "proyectos2024/index.html", {'memorias': memorias})

def cocos(request):
    return render(request, "proyectos2024/cocos.html")

def domotica(request):
    return render(request, "proyectos2024/domotica.html")

def empaquetadora(request):
    return render(request, "proyectos2024/empaquetadora.html")

def hidroponia(request):
    return render(request, "proyectos2024/hidroponia.html")

def riego(request):
    return render(request, "proyectos2024/riego.html")

def mapa(request):
    return render(request, "proyectos2024/mapa.html")