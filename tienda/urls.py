from django.urls import path
from . import views # Importamos las vistas creadas en tienda/views.py

urlpatterns = [
    path('', views.index, name='index'), # La ruta vacía es el inicio
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('perfil/', views.perfil, name='perfil'),
    path('carrito/', views.carrito, name='carrito'),
    path('mantenedor/', views.mantenedor_productos, name='mantenedor_productos'),
    path('categorias/accion/', views.accion, name='categorias_accion'),
    path('categorias/aventura/', views.aventura, name='categorias_aventura'),
    path('categorias/estrategia/', views.estrategia, name='categorias_estrategia'),
    path('categorias/supervivencia/', views.supervivencia, name='categorias_supervivencia'),
    path('categorias/disparos/', views.disparos, name='categorias_disparos'),
]

