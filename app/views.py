#Creamos en nuestro archivo views.py de la App las vistas

from django.shortcuts import render
from django.http import HttpResponse
from app.models import Especialistas

def index(req):
    return render(req,'appt/index.html')

def inicio(req):
    return render(req,'appt/contacto.html')

def especialista(req):
    return render(req,'appt/especialista.html')

def profesional(req):
    return render(req,'appt/profesional.html')

def paciente(req):
    return render(req,'appt/paciente.html')

def turno(req):
    return render(req,'appt/turnos.html')


def curso_form(req):
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
    
    

