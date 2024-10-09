"""
URL configuration for Projecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from Projecto1.views import saludo,otar_vista,probando_template,dia_de_hoy,agregar_especialista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('users/', include('users.urls')),
    path('saludo/', saludo),
    path('otra_vista/', otar_vista),
    path('plantillas/', probando_template),
    path('dia/', dia_de_hoy),
    path('agregar_esp/<especia>/<num>/', agregar_especialista),
]
