from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TrabajadorFormulario(forms.Form):
    run = forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    cargo = forms.CharField()
    imagen_cargo = forms.ImageField()