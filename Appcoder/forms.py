from django import forms

class HombreForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()

class BusquedaPersonaForm(forms.Form):

    nombre = forms.CharField()

