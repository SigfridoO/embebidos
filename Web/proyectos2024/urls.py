from django.urls import path
from .views import home, cocos, empaquetadora, domotica, hidroponia, riego, mapa


proyectos2024_urlpatterns = ([
    path('', home, name='home'),
   
    path('cocos/', cocos, name='cocos'),
    path('empaquetadora/', empaquetadora, name='empaquetadora'),
    path('domotica/', domotica, name='domotica'),
    path('hidroponia/', hidroponia, name='hidroponia'),
    path('riego/', riego, name='riego'),
    path('mapa/', mapa, name='mapa'),

], 'proyectos2024')