from django.shortcuts import render

# Vista de la página principal
def index(request):
    # 1. Creamos una variable y una lista de datos en Python
    nombre_gamer = "GamerX_99"
    lista_juegos = ["Super Mario Bros. Wonder", "Zelda: Tears of the Kingdom", "Monster Hunter Wilds"]
    
    # 2. Empaquetamos esos datos en un 'contexto' (diccionario)
    contexto = {
        "usuario": nombre_gamer,
        "juegos": lista_juegos
    }
    
    # 3. Enviamos el contexto al HTML
    return render(request, 'tienda/index.html', contexto)

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