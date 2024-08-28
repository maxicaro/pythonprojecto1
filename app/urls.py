from app import views
from django.urls import path

urlpatterns = [
    path('index/',views.index, name='index'),
    path('contacto/',views.inicio, name='contacto'),
    path('especialista/',views.especialista, name='especialista'),
    path('profesional/',views.profesional, name='profesional'),
    path('paciente/',views.paciente, name='paciente'),
    path('turno/',views.turno, name='turno'),
    path('especialista_form/',views.especialista_form, name='EspecialitaForm'),
    path('busqueda/',views.busqueda, name='busqueda'),
    path('buscar/',views.buscar),
]
