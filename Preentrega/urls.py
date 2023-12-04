
from django.contrib import admin
from django.urls import path
from Appcoder.views import  show_html, agregar_persona, mostrar_persona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', show_html),
    path('crear/', agregar_persona),
    # path('mostrar/', mostrar_persona)
]
