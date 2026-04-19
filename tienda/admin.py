from django.contrib import admin
from .models import Rol, PerfilUsuario

# Registramos las tablas para que aparezcan en el panel visual
admin.site.register(Rol)
admin.site.register(PerfilUsuario)