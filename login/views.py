from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

# Imports Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout

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