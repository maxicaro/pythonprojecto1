from app import views
from django.urls import path

urlpatterns = [
    path('index',views.index),
    path('inicio',views.inicio),
    path('especialista',views.especialista),
    path('profesional',views.profesional),
    path('paciente',views.paciente),
    path('turno',views.turno),
    
]
