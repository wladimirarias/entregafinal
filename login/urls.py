from django.urls import path
from login.views import *
from app.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("inicio/", iniciar_sesion, name="auth-login"),
    path("logout/", cerrar_sesion, name="auth-logout")
]