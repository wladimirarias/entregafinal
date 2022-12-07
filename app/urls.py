from django.urls import path
from app.views import *
from login.views import *

urlpatterns = [
    path("inicio/", inicio,  name="app-inicio"),
    path("logout/", cerrar_sesion, name="auth-logout"),
    path("login/", iniciar_sesion, name="auth-login"),
    path("editar/perfil/", editar_perfil, name="auth-editar-perfil"),
    path("editar/contrasena/", editar_contrasena, name="auth-editar-contrasena"),
    path("editar/avatar/", agregar_avatar, name="auth-avatar"),

    path("lista_trabajadores/", lista_trabajadores, name="app-list-trabajadores"),
    path("agregar_trabajador/", agregar_trabajador, name="app-agregar-trabajador"),
    path("editar_trabajador/<id>", editar_trabajador, name="app-editar-trabajador"),
    path("confirm_eliminar_trabajador/<id>", confirmar_eliminar_trabajador, name="app-confirm-eliminar-trabajador"),
    path("eliminar_trabajador/<id>", eliminar_trabajador, name="app-eliminar-trabajador"),
    path("detalle_trabajador/<id>", detalle_trabajador, name="app-detalle-trabajador")
]