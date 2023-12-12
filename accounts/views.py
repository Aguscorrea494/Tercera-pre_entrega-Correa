from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import UpdateView

from accounts.forms import UserRegisterForm, UserUpdateForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid(): #validamos el formulario que sea correcto
            data = form.cleaned_data #limpiamos el fomulario creando un dict
            usuario = data.get('username') #capturamos los datos que nos pasaron y se crea el dict
            contrasenia = data.get('password')
            user = authenticate(username=usuario, password= contrasenia) # COMPARAMOS LOS DATOS Y LA CONTRASENIA CON LOS DATOS DEL A BASE DE DATOS

            if user: # VALIDA SI EL USUARIO COINCIDE CON EL LOS DATOS DEL DIC
                login(request,user) # DA ACCESO

        return redirect("/app/lista")

    form = AuthenticationForm # SE PASA UN FORMULARIO PROPIO DE DJANGO HAY QUE IMPORTARLO
    contexto = {
        "form" : form
    }
    return render(request, template_name= "Accounts/login.html", context= contexto)

def register_request(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # SOLO GUARDA LA INFO, NO COMPARA COMO EL LOGIN

            return redirect("/accounts/login/") # REDIRIGE AL INGRESO

    form = UserRegisterForm()

    contexto = {
        "form" : form
    }
    return render(request, template_name="Accounts/register.html", context= contexto)


class UserSettings(UpdateView):
    pass
