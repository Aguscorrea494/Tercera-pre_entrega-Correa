
from django.contrib import admin
from django.urls import path
from Appcoder.views import  show_html, crear_persona_form, crear_persona, mostrar, busqueda_nombre, HombreList, HombreDetalle

urlpatterns = [
    path('show/', show_html),
    path('agregar/', crear_persona_form),
    path('buscar/', busqueda_nombre),
    path('crear/', crear_persona),
    # path('mostrar/', mostrar),
    path('mostrar1/', HombreList.as_view(), name= "HombreView"),
    path(r'^/(?P<pk>\d+)$', HombreDetalle.as_view(), name="HombreDetails")
]
