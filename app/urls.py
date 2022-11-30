from django.urls import path
from app.views import *
from login.views import *

urlpatterns = [
    path("inicio/", inicio,  name="app-inicio"),
    path("logout/", cerrar_sesion, name="auth-logout"),
    path("login/", iniciar_sesion, name="auth-login")
]