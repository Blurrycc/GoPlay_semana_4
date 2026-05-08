from django.db import models
from django.contrib.auth.models import User
import os
import uuid
from django.core.exceptions import ValidationError



# Función 1: Generar un nombre único e irrepetible para que las imágenes no choquen
def renombrar_imagen(instance, filename):
    # Extraemos la extensión del archivo original (ej. '.jpg' o '.png')
    ext = filename.split('.')[-1]
    # Generamos un nombre aleatorio único con UUID (ej. 'f47ac10b58cc4372a5670e02b2c3d479.jpg')
    nombre_unico = f"{uuid.uuid4().hex}.{ext}"
    # Guardamos en la carpeta 'productos/' dentro de tu directorio media
    return os.path.join('productos/', nombre_unico)

# Función 2: Validar el tamaño y el formato (Riesgos de almacenamiento)
def validar_imagen(value):
    # 1. Validar tamaño (Máximo 2 MB en este ejemplo)
    limite_megabytes = 2
    if value.size > limite_megabytes * 1024 * 1024:
        raise ValidationError(f"La imagen es demasiado pesada. El tamaño máximo permitido es de {limite_megabytes}MB.")

    # 2. Validar formato seguro
    ext = os.path.splitext(value.name)[1].lower()
    formatos_permitidos = ['.jpg', '.jpeg', '.png', '.webp']
    if ext not in formatos_permitidos:
        raise ValidationError(f"Formato no soportado. Por favor sube una imagen en formato: {', '.join(formatos_permitidos).upper()}")
    


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
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')

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
    imagen = models.ImageField(upload_to=renombrar_imagen, null=True, blank=True, verbose_name='Imagen del Juego', validators=[validar_imagen])

    def __str__(self):
        return self.nombre
    