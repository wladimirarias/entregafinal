from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.models import Avatar
from app.models import Trabajadores, Empresa, Obra
from app.forms import TrabajadorFormulario

#Import vistas basadas en clases para eliminar y mostrar detalle

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

def editar_trabajador(request, id):
    trabajador = Trabajadores.objects.get(id=id)

    if request.method == 'POST':
        formulario = TrabajadorFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data

            trabajador.run = data["run"]
            trabajador.nombre = data["nombre"]
            trabajador.apellido = data["apellido"]
            trabajador.edad = data["edad"]
            trabajador.email = data["email"]
            trabajador.cargo = data["cargo"]
            trabajador.imagen_cargo = data["imagen_cargo"]
            trabajador.save()
            return redirect("app-list-trabajadores")
        else:
            return render(request, "app/editar_trabajador.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = TrabajadorFormulario(initial={"run":trabajador.run, "nombre":trabajador.nombre,"apellido":trabajador.apellido,"edad":trabajador.edad,"email":trabajador.email,"cargo":trabajador.cargo,"imagen_cargo":""})
        return render(request, "app/editar_trabajador.html", {"formulario":formulario, "errores":""})

def confirmar_eliminar_trabajador(request, id):
    trabajador_model = Trabajadores.objects.filter(id=id).order_by("-id")

    if len(trabajador_model) > 0:
        trabajador = trabajador_model[0]
    else:
        trabajador = ""
    
    return render(request, "app/confirm_eliminar_trabajador.html", {"trabajador": trabajador})

def eliminar_trabajador(request, id):
    trabajador = Trabajadores.objects.get(id=id)
    trabajador.delete()

    return redirect("app-list-trabajadores")

def detalle_trabajador(request, id):
    trabajador_model = Trabajadores.objects.filter(id=id)

    if len(trabajador_model) > 0:
        trabajador = trabajador_model[0]
    else:
        trabajador = ""


    imagen_model = Trabajadores.objects.filter(id=id)

    if len(imagen_model) > 0:
        imagen_url = imagen_model[0].imagen_cargo.url
    else:
        imagen_url = ""

    
    #return render(request, "app/index.html", {"imagen_url": imagen_url})
    
    return render(request, "app/detalle_trabajador.html", {"trabajador": trabajador, "imagen_url": imagen_url})