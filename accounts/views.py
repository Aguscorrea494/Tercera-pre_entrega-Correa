from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.forms import UserRegisterForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid(): #validamos el formulario que sea correcto
            data = form.cleaned_data #limpiamos el fomulario creando un dict
            usuario = data.get('username') #capturamos los datos que nos pasaron y se crea el dict
            contrasenia = data.get('password')
            user = authenticate(username=usuario, password= contrasenia) # y autenticamos esos datos #se completan los datos del dicccionario

            if user: #guarda el usuario
                login(request,user)

        return redirect("/app/lista")

    form = AuthenticationForm
    contexto = {
        "form" : form
    }
    return render(request, template_name= "Accounts/login.html", context= contexto)

def register_request(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/accounts/login/")

    form = UserRegisterForm()

    contexto = {
        "form" : form
    }
    return render(request, template_name="Accounts/register.html", context= contexto)

