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
    path('leer_especialista/',views.leerEspecialista, name='leer_especialista'),
    path('eliminarespecialista/<especialista_nombre>/',views.eliminarEspecialista, name='Eliminarespecialista'),
     
     
    path('curso/list', views.CursoList.as_view(), name='List'),
    path('curso/<int:pk>/', views.CursoDetalle.as_view(), name='Detail'),
    path('nuevo/', views.CursoCreacion.as_view(), name='New'),
    path('curso/editar/<int:pk>/', views.CursoUpdate.as_view(), name='Edit'),
    path('curso/borrar/<int:pk>/', views.CursoDelete.as_view(), name='Delete'),
]



