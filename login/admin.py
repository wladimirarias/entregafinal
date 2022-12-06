from django.contrib import admin

from app.models import *
from login.models import *

# Register your models here.

admin.site.register(Avatar)
admin.site.register(Trabajadores)
admin.site.register(Empresa)
admin.site.register(Obra)