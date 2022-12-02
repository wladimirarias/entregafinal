from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.models import Avatar

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