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
    


# 3. Tabla para las Categorías de los juegos (Ej: Acción, Aventura, RPG)
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre de la Categoría')

    def __str__(self):
        return self.nombre

# 4. Tabla para los Productos (Videojuegos)
class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Título del Juego')
    descripcion = models.TextField(verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Stock Disponible')
    # Relacionamos cada juego con una categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    # Guardaremos las imágenes en una carpeta llamada 'productos'
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True, verbose_name='Imagen del Juego')

    def __str__(self):
        return self.nombre
    

