from django.db import models

#CREAMOS LAS TABLAS:

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
