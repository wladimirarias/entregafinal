from django.urls import path
from login.views import *
from app.views import *

urlpatterns = [
    path("inicio/", iniciar_sesion,  name="login-inicio")
]