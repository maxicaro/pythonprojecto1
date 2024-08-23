#Creamos en nuestro archivo views.py de la App las vistas

from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return render(req,'appt/index.html')

def inicio(req):
    return render(req,'appt/inicio.html')


def especialista(req):
    return render(req,'appt/especialista.html')

def profesional(req):
    return render(req,'appt/profesional.html')

def paciente(req):
    return render(req,'appt/paciente.html')

def turno(req):
    return render(req,'appt/turnos.html')

