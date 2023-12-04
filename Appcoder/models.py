from django.db import models

class Hombre(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.IntegerField()
    dni = models.IntegerField()


class Mujer(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.IntegerField()
    dni = models.IntegerField()

class Niño(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.IntegerField()
    dni = models.IntegerField()