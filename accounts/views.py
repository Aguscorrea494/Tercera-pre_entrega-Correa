from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import UpdateView

from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from accounts.models import Avatar


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

@login_required
def update_request(request):

    user = request.user

    if request.method == "POST":
        form = UserUpdateForm(request, POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = request.POST["email"]
            user.last_name = request.POST["last_name"]
            user.first_name = request.POST["first_name"]
            user.save()
            return redirect("/app/lista/")


    form = UserUpdateForm(initial={"username": user.username, "email": user.email,"last_name": user.last_name, "first_name": user.first_name})
    contexto = {

        "form" : form
    }
    return render(request, template_name="Accounts/register.html", context= contexto)

@login_required
def update_avatar(request):
    user = request.user
    if request.method == "POST":
        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
            except:
                avatar = Avatar(
                    user=user,
                    imagen = data["imagen"]
                )
            avatar = user.avatar
            avatar.save()

            return redirect("/app/lista")

    form = AvatarUpdateForm()
    contexto = {
       "form" : form
   }
    return render(request, template_name="Accounts/avatar.html" , context= contexto)






