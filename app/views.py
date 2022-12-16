from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.models import Avatar
from app.models import Trabajadores, Empresa, Obra, Mensajes
from app.forms import TrabajadorFormulario, MensajeFormulario

#Import de Fecha actual
from datetime import datetime

#Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

#Protección por sesiones
from django.contrib.auth.decorators import login_required

@login_required
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

def about(request):
    return render(request, "app/about.html")

@login_required
def lista_trabajadores(request):

    errores = ""

    trabajadores = Trabajadores.objects.all().order_by("nombre")
    contexto = {"listado_trabajadores": trabajadores, "errores": errores}

    return render(request, "app/trabajadores.html", contexto)

@login_required
def agregar_trabajador(request):
    now = datetime.now()
    
    if request.method == "POST":
        formulario = TrabajadorFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = request.user
            trabajador = Trabajadores(run=data["run"], nombre=data["nombre"], apellido=data["apellido"], edad=data["edad"], cargo=data["cargo"], email=data["email"], imagen_cargo=data["imagen_cargo"], fecha_ingreso=now ,user=usuario)
            trabajador.save()
            return redirect("app-inicio")
        else:
            return render(request, "app/agregar_trabajador.html", {"form": formulario, "errors": formulario.errors})
    
    formulario = TrabajadorFormulario()

    return render(request, "app/agregar_trabajador.html", {"form": formulario})

@login_required
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

@login_required
def confirmar_eliminar_trabajador(request, id):
    trabajador_model = Trabajadores.objects.filter(id=id).order_by("-id")

    if len(trabajador_model) > 0:
        trabajador = trabajador_model[0]
    else:
        trabajador = ""
    
    return render(request, "app/confirm_eliminar_trabajador.html", {"trabajador": trabajador})

@login_required
def eliminar_trabajador(request, id):
    trabajador = Trabajadores.objects.get(id=id)
    trabajador.delete()

    return redirect("app-list-trabajadores")

@login_required
def detalle_trabajador(request, id):
    trabajador_model = Trabajadores.objects.filter(id=id).select_related("user")

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

@login_required
def buscar_trabajador(request):
    return render(request, "app/busqueda_trabajadores.html")

@login_required
def resultados_busqueda_trabajadores(request):
    nombre_trabajador = request.GET["nombre_trabajador"]

    trabajadores = Trabajadores.objects.filter(nombre__icontains=nombre_trabajador)
    return render(request, "app/resultados_busqueda_trabajadores.html", {"trabajadores": trabajadores})

@login_required
def mensajeria(request):
    errores = ""
    now = datetime.now()

    if request.method == 'POST':
        formulario = MensajeFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = request.user
            mensaje = Mensajes(texto_mensaje=data["texto_mensaje"], fecha_ingreso=now, user=usuario)
            mensaje.save()
        else:
            errores = formulario.errors

    mensajes = Mensajes.objects.all().order_by("-id")
    formulario = MensajeFormulario()

    contexto = {"listado_mensajes": mensajes, "formulario": formulario ,"errores": errores}

    return render(request, "app/listado_mensajes.html", contexto)