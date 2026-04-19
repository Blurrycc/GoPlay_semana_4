from django.db import models
from django.contrib.auth.models import User

# 1. Tabla para los Roles (Administrador, Cliente, etc.)
class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre del Rol')

    def __str__(self):
        return self.nombre

# 2. Tabla para el Perfil (Extiende la tabla User que ya trae Django)
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name='Teléfono')
    direccion = models.CharField(max_length=200, blank=True, null=True, verbose_name='Dirección de Despacho')

    def __str__(self):
        return self.user.username