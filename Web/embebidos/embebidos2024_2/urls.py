from django.urls import path
from .views import home, cocos, empaquetadora, domotica, hidroponia, mapa


concurso_urlpatterns = ([
    path('', ConcursoView.as_view(), name='main'),
    path('login', ConcursoLoginView.as_view(), name='login'),
    path('logout', ConcursoLoginView.as_view(), name='logout'),
    path('registro', ConcursoRegistroView.as_view(), name='registro'),


    path('', views.home, name='home'),
    
    path('cocos/', views.cocos, name='cocos'),
    path('empaquetadora/', views.empaquetadora, name='empaquetadora'),
    path('domotica/', views.domotica, name='domotica'),
    path('hidroponia/', views.hidroponia, name='hidroponia'),
    path('mapa/', views.mapa, name='mapa'),



], 'concurso')