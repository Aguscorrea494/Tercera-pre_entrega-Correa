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
    persona = Hombre(nombre="Celina", apellido="Ramos", dni=43446736)
    persona.save()

    return redirect("/app/mostrar/")


def show_html(request):
    persona = Hombre.objects.first()
    contexto = {
        "persona": persona
    }
    return render(request, template_name="base.html", context=contexto)

@login_required #decorador captura el llamado de la funcion y valida
def crear_persona_form(request):
    if request.method == "POST":
        censo_formulario = HombreForm(request.POST)
        if censo_formulario.is_valid():
            informacion = censo_formulario.cleaned_data
            persona_agregar = Hombre(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"])
            persona_agregar.save()
            return redirect("/app/lista/")

    censo_formulario = HombreForm()
    contexto = {
        "form": censo_formulario
    }
    return render(request, template_name="Appcoder/censo.html", context=contexto)

def busqueda_nombre(request):
   nombre = request.GET["nombre"]
   persona = Hombre.objects.filter(nombre__icontains= nombre)
   contexto = {

       "personas": persona ,
       "form": BusquedaPersonaForm()
   }
   return render(request, template_name="Appcoder/personas.html", context=contexto)


class HombreList(LoginRequiredMixin, ListView):
    model = Hombre
    template_name = "Appcoder/censo1.html"

class HombreDetalle(LoginRequiredMixin, DetailView):
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

