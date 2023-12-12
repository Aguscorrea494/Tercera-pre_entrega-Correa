from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Appcoder.models import Hombre, Mujer, Niño
from Appcoder.forms import HombreForm, BusquedaPersonaForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def mostrar(request):
    persona = Hombre.objects.all()
    contexto = {
        "personas": persona,
        "form" : BusquedaPersonaForm()
    }
    return render(request, template_name="Appcoder/personas.html", context=contexto)


def crear_persona(request):
    persona = Hombre(nombre="Celina", apellido="Ramos", dni=43446736) # SE CREA PERSONA DE FORMA DIRECTA
    persona.save() # SE GUARDA EN BASE DE DATOS

    return redirect("/app/mostrar/")


def show_html(request):
    persona = Hombre.objects.first() #BUSCA EN BASE DE DATOS Y TRAES EL PRIMERO DE LA LISTA DE PERSONAS
    contexto = {
        "persona": persona
    }
    return render(request, template_name="base.html", context=contexto)

@login_required #decorador captura el llamado de la funcion y valida
def crear_persona_form(request):
    if request.method == "POST":  #5 SE VALIDA SI EL METODO ES POST
        censo_formulario = HombreForm(request.POST) # SE ACLARA EL TIPO
        if censo_formulario.is_valid(): # SE VALIDA SI EL FORMULARIO FUNCIONA
            informacion = censo_formulario.cleaned_data # SE TOMAN SOLO LOS DATOS LIMPIOS
            persona_agregar = Hombre(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"]) # SE LE PASAN LOS VALORES HTML AL FORMULARIO
            persona_agregar.save() #6 SE COMPLETA EL FORMULARIO CON LA DATA TRAIDA DEL FORMULARIO DE HTML
            return redirect("/app/lista/") #7 SE REDIRIGE A LA PAGINA DE LA LISTA

    censo_formulario = HombreForm() #1  SE ENVIA EN FORMULARIO EN FORMA GET A JGANGO PARA QUE SE VIZUALICE EN EL HTML
    contexto = {
        "form": censo_formulario #2 PARA QUE HTML LO PUEDA LEER
    }
    return render(request, template_name="Appcoder/censo.html", context=contexto) # SE LO PASA A HTML

def busqueda_nombre(request):
   nombre = request.GET["nombre"]
   persona = Hombre.objects.filter(nombre__icontains= nombre)
   contexto = {

       "personas": persona ,
       "form": BusquedaPersonaForm()
   }
   return render(request, template_name="Appcoder/personas.html", context=contexto)


class HombreList(LoginRequiredMixin, ListView): #LOGINREQUIREDMIXIN HACE REFERENCIA A QUE EL USUARIO DEBE ESTAR CON LA SESION INICIADA PARA ACCEDER
    model = Hombre
    template_name = "Appcoder/censo1.html"

class HombreDetalle(LoginRequiredMixin, DetailView): # MUESTRA MAS INFO DE LAS PERSONAS AGREGADAS
    model = Hombre
    template_name = "Appcoder/hombre_detalle.html"

class HombreCreacion(CreateView):
    model = Hombre
    success_url = "/app/lista/"
    template_name = ("Appcoder/censo.html")
    fields = ["nombre","apellido","dni"]

class HombreActualizacion(UpdateView):
    model = Hombre
    success_url = "/app/lista/"
    template_name = ("Appcoder/censo.html")
    fields = ["nombre","apellido","dni"]

class HombreEliminar(DeleteView):
    model = Hombre
    success_url = "/app/lista/"
    template_name = "Appcoder/eliminar_persona.html"

