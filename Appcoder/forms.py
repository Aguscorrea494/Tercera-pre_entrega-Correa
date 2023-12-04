from django import forms

class Agregar_Persona:
    nombre = forms.CharField
    apellido = forms.CharField
    dni = forms.IntegerField
