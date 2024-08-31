NAVEGACION:

En el archivo padre.html esta la plantilla y en la seccion nav estan los enlaces para navegar
-Ejemplo:
Turnos

-Con el name = ‘turno’ que esta en el archivio urls.py del phat
path(‘especialista/‘,views.especialista, name=’turno’)

llamamos a la funcion ef turno(req):
return render(req,’appt/turnos.html’)
del arcivo vews.py y renderisamos los html.
ADMISTRADOR DE DJANGO:

En el archivo admin.py estan importados los modelos tablas(clases)
para poder registrar los datos :

from django.contrib import admin
from app.models import Especialistas,paciente,profesional,turnos
REGISTRAR MODELOS.

from django.contrib import admin
from app.models import Especialistas,paciente,profesional,turnos

admin.site.register(Especialistas)
admin.site.register(paciente)
admin.site.register(profesional)
admin.site.register(turnos)

TE DEJO UN VIDEO PARA EXPLICAR MAS A DETALLE CON LA PAGINA CORRIENDO:

Links:
https://drive.google.com/file/d/1WFn1n3Z-OyNWidIBQxxOW9H5OJd6_nyO/view?usp=sharing
