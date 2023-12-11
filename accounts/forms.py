from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta: # Es para modicar el formulario
        model = User
        fields = ("username", "email")
