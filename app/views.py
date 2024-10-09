#Creamos en nuestro archivo views.py de la App las vistas

from typing import List

from django.shortcuts import render
from django.http import HttpResponse
from app.models import Especialistas

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Decorador por defecto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(req):
    return render(req, 'appt/index.html')

@login_required
def inicio(req):
    return render(req, 'appt/contacto.html')

@login_required
def especialista(req):
    return render(req, 'appt/especialista.html')

@login_required
def profesional(req):
    return render(req, 'appt/profesional.html')

@login_required
def paciente(req):
    return render(req, 'appt/paciente.html')

@login_required
def turno(req):
    return render(req, 'appt/turnos.html')

def especialista_form(req):
    mensaje = ''
    if req.method == 'POST':
        
        especialista = Especialistas(nombre=req.POST['nombre'], codigo=req.POST['codigo'])
        
        especialista.save()
        
        # Establece el mensaje de éxito
        mensaje = '¡Te has inscripto correctamente!'
    else:
            # Mensaje para campos incompletos
            mensaje = '¡Por favor complete los campos!'

    # Renderiza el formulario con el mensaje en el contexto
    return render(req, 'appt/formulario.html', {'mensaje': mensaje})

def busqueda(request):
    return render(request,'appt/busqueda.html')
        
def buscar(request):
    
 if request.GET["codigo"]:
    
    codigo = request.GET["codigo"]
    
    nombre = Especialistas.objects.filter(codigo__contains=codigo)
    
    return render(request, "appt/resultadoBusqueda.html", {"nombre": nombre, "codigo": codigo})

 else:
       
       respuesta = "No enviaste datos"
       
       return HttpResponse(respuesta)
    
    
def leerEspecialista(request):

      esp = Especialistas.objects.all() #trae todos los profesionales

      contexto= {"Especialistas":esp} 

      return render(request, 'appt/leer_especialista.html',contexto)
  
  
  
def eliminarEspecialista(request, especialista_nombre):
    
    especia = Especialistas.objects.filter(nombre=especialista_nombre).first()
    especia.delete()
    
    especia = Especialistas.objects.all() #trae todos los profesionales

    contexto= {"Especialistas":especia} 

    return render(request, 'appt/leer_especialista.html',contexto)
  
#VISTAS DE CLASES:
class CursoList(LoginRequiredMixin, ListView):

     model = Especialistas 
     template_name = "appt/especialista_list.html"



class CursoDetalle(DetailView):

      model = Especialistas
      template_name = "appt/curso_detalle.html"
     

class CursoCreacion(CreateView):

      model = Especialistas
      template_name = 'appt/curso_form.html'
      success_url =  reverse_lazy("List")
      #success_url = "/appt/curso/list"
      fields = ['nombre', 'codigo']


class CursoUpdate(UpdateView):

      model = Especialistas
      template_name = 'appt/curso_form.html'
      success_url =  reverse_lazy("List")
     # success_url = "/appt/curso/list"
      fields  = ['nombre', 'codigo']


class CursoDelete(DeleteView):

      model = Especialistas
      success_url =  reverse_lazy("List")
      template_name = 'appt/curso_confirm_delete.html'




