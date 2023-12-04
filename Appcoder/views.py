from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Hombre, Mujer, Niño
from Appcoder.forms import Agregar_Persona


def mostrar_persona(request):
    persona = Hombre(nombre = "Agustin", apellido = "Correa", dni = 43456736)

    Hombre.save
    return HttpResponse(f"su nombre es{persona.nombre} con apellido{persona.apellido}, y dni {persona.dni}")



def show_html(request):
    persona = Hombre.objects.all()
    contexto = {"Persona": Hombre}
    return render(request, template_name= "base.html", context=contexto)

def agregar_persona(request):
    formulario_censo = Agregar_Persona
    contexto = {
        "form" : agregar_persona
    }
    return render(request, template_name= "Appcoder/censo.html", context= contexto)




