
from django.contrib import admin
from django.urls import path
from Appcoder.views import  show_html, crear_persona_form, crear_persona, mostrar, busqueda_nombre

urlpatterns = [
    path('show/', show_html),
    path('agregar/', crear_persona_form),
    path('buscar/', busqueda_nombre),
    path('crear/', crear_persona),
    path('mostrar/', mostrar),
]
