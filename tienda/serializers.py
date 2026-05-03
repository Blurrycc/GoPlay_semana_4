from rest_framework import serializers
from .models import Categoria, Producto

# Serializador para API: Categorías
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__' # Esto exportará todos los campos de la categoría (ID, nombre)

# Serializador para API 2: Productos del Catálogo
class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'categoria_nombre', 'imagen']
        # Esto exportará los campos del producto, incluyendo el nombre de la categoría para facilitar su lectura en la API  

