from django.shortcuts import render, redirect
from login.models import Avatar
from login.forms import UserEditForm, UserEditFormPass, AvatarForm, UserRegisterForm
from django.http import HttpResponse
from django.http import Http404


# Imports Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password, check_password

# Función para Inicio de Sesión
def iniciar_sesion(request):

    errors = ""

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            user = authenticate(username = data["username"], password = data["password"])

            if user is not None:
                login(request,user)
                return redirect("app-inicio")
            else:
                return render(request, "login/login.html", {"form": formulario, "errors": "Credenciales Inválidas"})
        else:
            return redirect("auth-login")
    
    formulario = AuthenticationForm()
    return render(request, "login/login.html", {"form": formulario, "errors": errors})

def cerrar_sesion(request):
    logout(request)
    return redirect("auth-login")

def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.save()

            return redirect("app-inicio")
        else:
            return render(request, "app/editar_perfil.html", {"form": formulario, "errors": formulario.errors})
    else:
        formulario = UserEditForm(initial = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})
    
    return render(request, "app/editar_perfil.html", {"form": formulario})

def editar_contrasena(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditFormPass(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.password = make_password(data["password1"])
            usuario.save()

            return redirect("auth-login")
        else:
            return render(request, "app/editar_perfil_contrasena.html", {"form": formulario, "errors": formulario.errors})
    else:
        formulario = UserEditFormPass()
    
    return render(request, "app/editar_perfil_contrasena.html", {"form": formulario})

def agregar_avatar(request):

    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = request.user
            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()
            return redirect("app-inicio")
        else:
            return render(request, "app/agregar_avatar", {"form": formulario, "errors": formulario.errors})
    
    formulario = AvatarForm()

    return render(request, "app/agregar_avatar.html", {"form": formulario})

def registrar_usuario(request):

    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)

        pass