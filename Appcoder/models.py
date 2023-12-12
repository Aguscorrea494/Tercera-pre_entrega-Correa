from django.db import models

class Hombre(models.Model): # SE CREA MODELOS CON SUS CARACTERISTICAS
     nombre = models.CharField(max_length=40)
     apellido = models.CharField(max_length=30)
     dni = models.IntegerField()


     def __str__(self):
        return(self.nombre)



class Mujer(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()

class Niño(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()