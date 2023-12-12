from django.contrib.auth.views import LogoutView

from accounts.views import login_request, register_request

from django.urls import path


urlpatterns = [
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name= "Accounts/logout.html"), name="Logout"), # NO SE CREA VISTA SOLO SE LE AGREGA LOGOOUT QUE SE HEREDA EL PLANTILLA CON LA QUE SE QUIERE MOSTRAR
    path('register/', register_request, name="Register"),
    path('login/', login_request, name="Login")


]