from django.db import models

#CREAMOS LAS TABLAS:

class Especialistas(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()
    
    def __str__(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre}"

class paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Email: {self.email}"

class profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Email: {self.email} | Profesion: {self.profesion}"
    
class turnos(models.Model):
    nombre = models.CharField(max_length=30) 
    turno = models.DateField()
    atendido = models.BooleanField() 
    
    def __str__(self):
        return f"Nombre: {self.nombre} | Turno: {self.turno} | Atendido: {self.atendido}"

