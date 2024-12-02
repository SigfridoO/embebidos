"""
URL configuration for embebidos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings

from app.front.urls import urlpatterns_chat

from proyectos2024.urls import proyectos2024_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    
    # path('cocos/', views.cocos, name='cocos'),
    # path('empaquetadora/', views.empaquetadora, name='empaquetadora'),
    # path('domotica/', views.domotica, name='domotica'),
    # path('hidroponia/', views.hidroponia, name='hidroponia'),
    # path('riego/', views.riego, name='riego'),
    # path('mapa/', views.mapa, name='mapa'),

    path('proyectos2024/', include(proyectos2024_urlpatterns)),

    path('chat/', include(urlpatterns_chat)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    
    urlpatterns += static (settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)