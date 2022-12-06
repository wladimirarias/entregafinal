from django.db import models
from django.contrib.auth.models import User

class Trabajadores(models.Model):
    run = models.IntegerField()
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    edad = models.IntegerField()
    email = models.EmailField()
    cargo = models.CharField(max_length=100)
    imagen_cargo = models.ImageField(upload_to="trabajadores", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Run Trabajador: {self.run} | Nombre Trabajador: {self.nombre.capitalize()} | Apellido Trabajador: {self.apellido.capitalize()} | Edad Trabajador: {self.edad} | Email Trabajador: {self.email.capitalize()} | Cargo Trabajador: {self.cargo.capitalize()} | URL Imagen: {self.imagen_cargo} | Usuario Registro: {self.user}"

class Empresa(models.Model):
    run = models.IntegerField()
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return f"Run Empresa: {self.run} | Nombre Empresa: {self.nombre.capitalize()} | Dirección Empresa: {self.direccion.capitalize()} | Email Empresa: {self.email.capitalize()}"

class Obra(models.Model):
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()
    fono = models.IntegerField()

    def __str__(self):
        return f"Nombre Obra: {self.nombre.capitalize()} | Dirección Obra: {self.direccion.capitalize()} | Email Obra: {self.email.capitalize()} | Fono Obra: {self.fono}"