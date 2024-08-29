#Tercera Pre-entega:

###Herencias HTML.
- En la carpeta APP/templates/appt estan los arcivos html heredados de padre los achivos son:
-especialista.html.
-profesional,html.
-contacto.html.
-tuno.html.

###Models.

Los modelos de datos  estan en la carpeta APP son 4:

class Especialistas(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()

class paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class turnos(models.Model):
    nombre = models.CharField(max_length=30) 

    turno = models.DateField()
    atendido = models.BooleanField() 

-Se uso el modelo  especialista para ingresar datos a traves del metodo POST y para obtenerlos con GET y tambien guardarlosl a funcion llamada def especialista_form(req): fue creada en el archivo views.py .


###Formularios.

-Con el archivo formulario.html ingresamos los datos a partir del modelo especialista ingresamos su nombre y codigo, en el archivo views.py esta creada la funicion especialista_form(req): con POTS para enviar los datos y guardarlos en la base de datos para poder obtnerlos.

-Con el formulario busqueda.html  buscamos el nombre del especialista y su codigo, tambien se agrego otro archivo llamado buscar.html para pode visualisar los datos la funcion def buscar(request): con el metodo GET obtenemos sus datos.



###Adicional 
-Agregue estilos a los formularios, al ingresar datos te da un mensaje de ingresaste los datos correctamente!!.
