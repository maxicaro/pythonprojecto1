#Tercera Pre-entega:

###Herencias HTML.
- En la carpeta APP/templates/appt están los arcivos html heredados de padre los achivos son:
-especialista.html.
-profesional,html.
-contacto.html.
-tuno.html.

###Modelos.

Los modelos de datos estan en la carpeta APP son 4:

clase Especialistas(modelos.Modelo):
    nombre = modelos.CharField(max_length=40)
    codigo = modelos.IntegerField()

clase paciente(modelos.Modelo):
    nombre = modelos.CharField(max_length=30)
    apellido = modelos.CharField(max_length=30)
    correo electrónico = modelos.EmailField()

clase profesional(modelos.Modelo):
    nombre = modelos.CharField(max_length=30)
    apellido = modelos.CharField(max_length=30)
    correo electrónico = modelos.EmailField()
    profesión = modelos.CharField(max_length=30)

clase turnos(modelos.Modelo):
    nombre = modelos.CharField(max_length=30)

    turno = modelos.DateField()
    atendido = modelos.BooleanField()

-Se utiliza el modelo especialista para ingresar datos a través del método POST y para obtenerlos con GET y también guardarlosl a función llamada def especialista_form(req): fue creada en el archivo views.py.


###Formularios.

-Con el archivo formulario.html ingresamos los datos a partir del modelo especialista ingresamos su nombre y código, en el archivo views.py esta creada la función especialista_form(req): con POTS para enviar los datos y guardarlos en la base de datos para poder obtenerlos.

-Con el formulario busqueda.html buscamos el nombre del especialista y su codigo, tambien se agrega otro archivo llamado buscar.html para poder visualizar los datos la funcion def buscar(request): con el metodo GET obtenemos sus datos.



###Adicional
-Agregue estilos a los formularios, al ingresar datos te da un mensaje de ingresaste los datos correctamente!!.
