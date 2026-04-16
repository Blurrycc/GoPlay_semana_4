from django.shortcuts import render

# Vista de la página principal
def index(request):
    return render(request, 'tienda/index.html')

# Vistas de Usuario
def login(request):
    return render(request, 'tienda/login.html')

def registro(request):
    return render(request, 'tienda/registro.html')

def recuperar(request):
    return render(request, 'tienda/recuperar.html')

def perfil(request):
    return render(request, 'tienda/perfil.html')

# Vistas de Tienda
def carrito(request):
    return render(request, 'tienda/carrito.html')

def mantenedor_productos(request):
    return render(request, 'tienda/mantenedor_productos.html')