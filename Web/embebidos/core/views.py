from django.shortcuts import render

def home(request):
    return render(request, "core/index.html")

def cocos(request):
    return render(request, "core/cocos.html")

def domotica(request):
    return render(request, "core/domotica.html")

def empaquetadora(request):
    return render(request, "core/empaquetadora.html")

def hidroponia(request):
    return render(request, "core/hidroponia.html")

def mapa(request):
    return render(request, "core/mapa.html")