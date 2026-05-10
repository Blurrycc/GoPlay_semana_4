from django.urls import path
from . import views # Importamos las vistas creadas en tienda/views.py
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token


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
    path('logout/', views.cerrar_sesion, name='logout'), # Ruta para cerrar sesión

    path('mantenedor/', views.mantenedor_productos, name='mantenedor'), # Ruta para el mantenedor de productos (solo admin)
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'), # Ruta para eliminar un producto (solo admin)
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'), # Ruta para editar un producto (solo admin)

    # --- RUTAS PARA RECUPERAR CONTRASEÑA ---
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="tienda/recuperar.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="tienda/recuperar_enviado.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="tienda/recuperar_confirmar.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="tienda/recuperar_completo.html"), name="password_reset_complete"),


    # Rutas para las APIs Propias
    path('api/categorias/', views.api_listar_categorias, name='api_categorias'),
    path('api/productos/', views.api_listar_productos, name='api_productos'),

    # Ruta para generar el Token de seguridad
    path('api/token/', obtain_auth_token, name='api_token'),

    # Rutas para las novedades (Uso de APIs externas)
    path('novedades/', views.novedades, name='novedades'),

    # Ruta dinámica para el detalle del producto:
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),

    # Rutas para el mantenedor de usuarios (solo admin)
    path('mantenedor-usuarios/', views.mantenedor_usuarios, name='mantenedor_usuarios'),
    path('editar-usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),


    # Rutas para las APIs externas (proxy)
    path('api/ofertas/', views.api_proxy_ofertas, name='api_ofertas'),
    path('api/coleccionables/', views.api_proxy_coleccionables, name='api_coleccionables'),

    # Ruta para mostrar productos por categoría
    path('categoria/<int:id_cat>/', views.productos_por_categoria, name='productos_por_categoria'),
]

