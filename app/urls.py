from django.urls import path
from app.views import *
from login.views import *

urlpatterns = [
    path("inicio/", inicio,  name="app-inicio")
]