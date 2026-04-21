from django.contrib import admin
from .models import Rol, PerfilUsuario
from .models import Rol, PerfilUsuario, Categoria, Producto

# Registramos las tablas para que aparezcan en el panel visual
admin.site.register(Rol)
admin.site.register(PerfilUsuario)
admin.site.register(Categoria)
admin.site.register(Producto)

