AVEGACION:

En el archivo padre.html esta la plantilla y en la sección nav están los enlaces para navegar -Ejemplo: Turnos

-Con el name = 'turno' que esta en el archivo urls.py del phat path('especialista/',views.especialista, name='turno')

llamamos a la funcion ef turno(req): return render(req,'appt/turnos.html') del arcivo vews.py y renderisamos los html. ADMINISTRADOR DE DJANGO:

En el archivo admin.py están importados los modelos tablas(clases) para poder registrar los datos:

desde django.contrib import admin desde app.models import Especialistas,paciente,profesional,turnos REGISTRAR MODELOS.

desde django.contrib importar admin desde app.models importar Especialistas,paciente,profesional,turnos

admin.site.register(Especialistas) admin.site.register(paciente) admin.site.register(profesional) admin.site.register(turnos)

TE DEJO UN VIDEO PARA EXPLICAR MAS A DETALLE CON LA PAGINA CORRIENDO:

Enlaces: https://drive.google.com/file/d/1WFn1n3Z-OyNWidIBQxxOW9H5OJd6_nyO/view?usp=sharing
