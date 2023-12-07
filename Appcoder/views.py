from django.shortcuts import render, redirect
from django.http import HttpResponse
from Appcoder.models import Hombre, Mujer, Niño
from Appcoder.forms import HombreForm, BusquedaPersonaForm


def mostrar(request):
    persona = Hombre.objects.all()
    contexto = {
        "personas": persona,
        "form" : BusquedaPersonaForm()
    }
    return render(request, template_name="Appcoder/personas.html", context=contexto)


def crear_persona(request):
    persona = Hombre(nombre="Celina", apellido="Ramos", dni=43446736)
    persona.save()

    return redirect("/app/mostrar/")


def show_html(request):
    persona = Hombre.objects.first()
    contexto = {
        "persona": persona
    }
    return render(request, template_name="base.html", context=contexto)


def crear_persona_form(request):
    if request.method == "POST":
        censo_formulario = HombreForm(request.POST)
        if censo_formulario.is_valid():
            informacion = censo_formulario.cleaned_data
            persona_agregar = Hombre(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"])
            persona_agregar.save()
            return redirect("/app/mostrar")

    censo_formulario = HombreForm()
    contexto = {
        "form": censo_formulario
    }
    return render(request, template_name="Appcoder/censo.html", context=contexto)

def busqueda_nombre(request):
   nombre = request.GET["nombre"]
   persona = Hombre.objects.filter(nombre__icontains= nombre)
   contexto = {

       "personas": persona,
       "form": BusquedaPersonaForm()
   }
   return render(request, template_name="Appcoder/personas.html", context=contexto)

