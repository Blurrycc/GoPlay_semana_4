from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PerfilUsuario
from django.contrib.auth import authenticate, login, logout

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
def login_usuario(request): # Le cambiamos el nombre ligeramente para que no choque con la función 'login' de Django
    if request.method == 'POST':
        # 1. Atrapamos los datos del formulario usando los "name" de nuestros inputs en HTML
        usuario_login = request.POST.get('alias_usuario')
        contrasena_login = request.POST.get('password_usuario')

        # 2. Django verifica si existe y si la clave es correcta
        user = authenticate(request, username=usuario_login, password=contrasena_login)

        if user is not None:
            # 3. Si todo está bien, le creamos la sesión (lo dejamos "logueado")
            login(request, user)
            return redirect('index') # Lo mandamos a la página principal
        else:
            # 4. Si se equivoca, mostramos un error
            messages.error(request, 'Usuario o contraseña incorrectos.')

    # Si solo está entrando a mirar la página, cargamos el HTML normal
    return render(request, 'tienda/login.html')

def registro(request):
    if request.method == 'POST':
        # 1. Atrapamos los datos usando los "name" de tus inputs en HTML
        alias = request.POST.get('alias_usuario')
        correo = request.POST.get('email_usuario')
        clave = request.POST.get('password_usuario')
        direccion = request.POST.get('direccion_envio')
        
        # 2. Guardamos el usuario base en la tabla de Django
        try:
            # create_user encripta la contraseña automáticamente
            nuevo_usuario = User.objects.create_user(username=alias, email=correo, password=clave)
            
            # 3. Guardamos los datos extra en tu tabla PerfilUsuario
            PerfilUsuario.objects.create(user=nuevo_usuario, direccion=direccion)
            
            # 4. Mensaje de éxito y redirección
            messages.success(request, '¡Cuenta creada exitosamente! Por favor, inicia sesión.')
            return redirect('login')
            
        except Exception as e:
            # Si el usuario ya existe o hay un error, mostramos un mensaje
            messages.error(request, 'Error al crear la cuenta. Intenta con otro nombre de usuario.')
            
    # Si el usuario solo entra a la página (método GET), mostramos tu HTML normal
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

# --- Vistas de Categorías ---
def accion(request):
    return render(request, 'tienda/categorias/accion.html')

def aventura(request):
    return render(request, 'tienda/categorias/aventura.html')

def estrategia(request):
    return render(request, 'tienda/categorias/estrategia.html')

def supervivencia(request):
    return render(request, 'tienda/categorias/supervivencia.html')

def disparos(request):
    return render(request, 'tienda/categorias/disparos.html')

