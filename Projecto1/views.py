from django.http import HttpResponse
from django.template import Template, Context
from datetime import date
from datetime import datetime
from django.template import loader
from app.models import Especialistas

def saludo(request):
    return HttpResponse("Hola Django - Coder")


def otar_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.<p>")


def dia_de_hoy(request):
    hoy = date.today()
    return HttpResponse(f"Hoy es {hoy}")


def probando_template(request):
    
    diccionario = {"hoy": datetime.now()}

   
    
    plantilla = loader.get_template('template1.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)


def agregar_especialista(request,especia, num):
    especialista = Especialistas(nombre=especia, codigo=num)
    especialista.save()
    
    return HttpResponse("Curso agragado")