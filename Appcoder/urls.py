
from django.contrib import admin
from django.urls import path
from Appcoder.views import show_html, crear_persona_form, crear_persona, mostrar, busqueda_nombre, HombreList, HombreDetalle, HombreCreacion, HombreActualizacion, HombreEliminar

urlpatterns = [
    path('show/', show_html),
    path('agregar/', crear_persona_form),
    path('buscar/', busqueda_nombre),
    path('crear/', crear_persona),
    # path('mostrar/', mostrar),
    path('lista/', HombreList.as_view(), name="HombreView"),
    path('persona/<int:pk>', HombreDetalle.as_view(), name="HombreDetail"),
    path('crear1/', HombreCreacion.as_view(), name="HombreCreate"),
    path('editar/<int:pk>', HombreActualizacion.as_view(), name="HombreUpdate"),
    path('eliminar/<int:pk>', HombreEliminar.as_view(), name="HombreDelate" )



]
