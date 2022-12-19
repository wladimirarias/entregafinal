from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea
from django.db import models

class TrabajadorFormulario(forms.Form):
    run = forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    cargo = forms.CharField()
    imagen_cargo = forms.ImageField(required=False)

class MensajeFormulario(forms.Form):
    texto_mensaje = forms.CharField(label="Mensaje")