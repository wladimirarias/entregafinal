from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.models import Avatar
from app.models import Trabajadores, Empresa, Obra
from app.forms import TrabajadorFormulario

#Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def inicio(request):

    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user=request.user.id).order_by("-id")

        if len(imagen_model) > 0:
            imagen_url = imagen_model[0].imagen.url
        else:
            imagen_url = ""
    else:
        imagen_url = ""
    
    return render(request, "app/index.html", {"imagen_url": imagen_url})

def lista_trabajadores(request):

    errores = ""

    trabajadores = Trabajadores.objects.all().order_by("nombre")
    contexto = {"listado_trabajadores": trabajadores, "errores": errores}

    return render(request, "app/trabajadores.html", contexto)

def agregar_trabajador(request):
    
    if request.method == "POST":
        formulario = TrabajadorFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = request.user
            trabajador = Trabajadores(run=data["run"], nombre=data["nombre"], apellido=data["apellido"], edad=data["edad"], cargo=data["cargo"], email=data["email"], imagen_cargo=data["imagen_cargo"], user=usuario)
            trabajador.save()
            return redirect("app-inicio")
        else:
            return render(request, "app/agregar_trabajador.html", {"form": formulario, "errors": formulario.errors})
    
    formulario = TrabajadorFormulario()

    return render(request, "app/agregar_trabajador.html", {"form": formulario})