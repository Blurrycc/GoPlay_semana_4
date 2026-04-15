from django.urls import path
from . import views # Importamos las vistas que acabamos de crear

urlpatterns = [
    # Si la ruta está vacía (''), carga la vista 'index'
    path('', views.index, name='index'),
]