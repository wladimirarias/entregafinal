from django.urls import path
from login.views import *
from app.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("inicio/", iniciar_sesion, name="auth-login"),
    path("logout/", cerrar_sesion, name="auth-logout"),
    path("editar/perfil/", editar_perfil, name="auth-editar-perfil"),
    path("editar/contrasena/", editar_contrasena, name="auth-editar-contrasena"),
    path("editar/avatar/", agregar_avatar, name="auth-avatar")
]