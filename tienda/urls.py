from django.urls import path
from . import views # Importamos las vistas creadas en tienda/views.py

urlpatterns = [
    path('', views.index, name='index'), # La ruta vacía es el inicio
    path('login/', views.login_usuario, name='login'), # Ruta para el login
    path('registro/', views.registro, name='registro'), # Ruta para el registro
    path('recuperar/', views.recuperar, name='recuperar'), # Ruta para recuperar contraseña
    path('perfil/', views.perfil, name='perfil'), # Ruta para el perfil de usuario
    path('carrito/', views.carrito, name='carrito'), # Ruta para el carrito de compras
    path('mantenedor/', views.mantenedor_productos, name='mantenedor_productos'), # Ruta para el mantenedor de productos (solo admin)
    path('categorias/accion/', views.accion, name='categorias_accion'), # Ruta para categoría Acción
    path('categorias/aventura/', views.aventura, name='categorias_aventura'), # Ruta para categoría Aventura
    path('categorias/estrategia/', views.estrategia, name='categorias_estrategia'), # Ruta para categoría Estrategia
    path('categorias/supervivencia/', views.supervivencia, name='categorias_supervivencia'), # Ruta para categoría Supervivencia
    path('categorias/disparos/', views.disparos, name='categorias_disparos'), # Ruta para categoría Disparos
]

