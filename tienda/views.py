from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PerfilUsuario, Producto, Categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Vista de la página principal
def index(request):
    return render(request, 'tienda/index.html')

# Vistas de Usuario
def login_usuario(request): # Le cambiamos el nombre ligeramente para que no choque con la función 'login' de Django
    if request.method == 'POST':
        # Atrapamos los datos del formulario usando los "name" de nuestros inputs en HTML
        usuario_login = request.POST.get('alias_usuario')
        contrasena_login = request.POST.get('password_usuario')

        # Django verifica si existe y si la clave es correcta
        user = authenticate(request, username=usuario_login, password=contrasena_login)

        if user is not None:
            # Si todo está bien, le creamos la sesión (lo dejamos "logueado")
            login(request, user)
            return redirect('index') # Lo mandamos a la página principal
        else:
            # Si se equivoca, mostramos un error
            messages.error(request, 'Usuario o contraseña incorrectos.')

    # Si solo está entrando a mirar la página, cargamos el HTML normal
    return render(request, 'tienda/login.html')

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import PerfilUsuario # Asegúrate de importar el nuevo modelo

def registro(request):
    if request.method == 'POST':
        # 1. Capturamos todos los datos del HTML
        v_nombre = request.POST.get('nombre_completo')
        v_username = request.POST.get('username')
        v_email = request.POST.get('email')
        v_password = request.POST.get('password')
        v_password_conf = request.POST.get('password_conf') # Capturamos la 2da clave
        
        v_direccion = request.POST.get('direccion') # Capturamos dirección
        v_fecha_nac = request.POST.get('fecha_nacimiento') # Capturamos fecha
        
        # 2. Verificar que las contraseñas coincidan
        if v_password != v_password_conf:
            messages.error(request, 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.')
            return redirect('registro')

        # 3. Comprobamos si el usuario o email ya existen
        if User.objects.filter(username=v_username).exists():
            messages.error(request, f'El nombre de usuario "{v_username}" ya está en uso.')
            return redirect('registro')

        if User.objects.filter(email=v_email).exists():
            messages.error(request, 'Este correo electrónico ya se encuentra registrado.')
            return redirect('registro')

        # 4. Validación de políticas de contraseña segura
        try:
            validate_password(v_password)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, f'Contraseña insegura: {error}')
            return redirect('registro')

        # 5. Creación del Usuario y su Perfil
        try:
            # Creamos el usuario base de Django
            nuevo_usuario = User.objects.create_user(
                username=v_username, 
                email=v_email, 
                password=v_password
            )
            nuevo_usuario.first_name = v_nombre
            nuevo_usuario.save()

            # Creamos el perfil extendido con la dirección y fecha
            # Validamos si vino vacía la fecha para no romper la base de datos
            if v_fecha_nac == "":
                v_fecha_nac = None

            PerfilUsuario.objects.create(
                user=nuevo_usuario,
                direccion=v_direccion,
                fecha_nacimiento=v_fecha_nac
            )

            messages.success(request, '¡Tu cuenta Go Play! ha sido creada exitosamente. Ya puedes iniciar sesión.')
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f'Ocurrió un error al crear la cuenta: {str(e)}')
            return redirect('registro')

    return render(request, 'tienda/registro.html')

def recuperar(request):
    return render(request, 'tienda/recuperar.html')


# --- Vistas Protegidas ---
@login_required(login_url='login')
def perfil(request):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre_completo')
        nuevo_correo = request.POST.get('email_usuario')
        nueva_clave = request.POST.get('password_nueva') # Atrapamos la nueva clave del HTML
        
        usuario = request.user
        usuario.first_name = nuevo_nombre
        usuario.email = nuevo_correo
        
        # Lógica para cambiar contraseña solo si el usuario escribió algo
        if nueva_clave and nueva_clave.strip() != '':
            usuario.set_password(nueva_clave) # Encripta la nueva clave para Oracle
            usuario.save()
            update_session_auth_hash(request, usuario) # Mantiene al usuario logueado con su nueva clave
        else:
            usuario.save() # Guarda solo nombre y correo
            
        messages.success(request, '¡Tus datos han sido actualizados con éxito!')
        return redirect('perfil')

    return render(request, 'tienda/perfil.html')

# Vistas de Tienda
@login_required(login_url='login')
def carrito(request):
    return render(request, 'tienda/carrito.html')

@login_required(login_url='login')
def mantenedor_productos(request):
    # 1. Seguridad: Si el usuario NO es administrador (staff), lo echamos
    if not request.user.is_staff:
        messages.error(request, 'Acceso denegado. Esta sección es solo para Administradores.')
        return redirect('index')

    # 2. Traemos los datos de Oracle
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    # 3. Lógica para CREAR un producto nuevo desde el Frontend
    if request.method == 'POST':
        v_nombre = request.POST.get('nombre_prod')
        v_desc = request.POST.get('desc_prod', 'Sin descripción') # Por si no tienes campo de descripción
        v_precio = request.POST.get('precio_prod')
        v_stock = request.POST.get('stock_prod')
        v_cat_id = request.POST.get('categoria_prod')
        
        # Las imágenes no viajan en POST, viajan en FILES
        v_imagen = request.FILES.get('imagen_prod') 

        try:
            categoria_obj = Categoria.objects.get(id=v_cat_id)
            Producto.objects.create(
                nombre=v_nombre,
                descripcion=v_desc,
                precio=v_precio,
                stock=v_stock,
                categoria=categoria_obj,
                imagen=v_imagen
            )
            messages.success(request, '¡Producto agregado al catálogo exitosamente!')
            return redirect('mantenedor')
        except Exception as e:
            messages.error(request, f'Error al guardar: {str(e)}')

    # 4. Enviamos los datos al HTML
    contexto = {
        'categorias': categorias,
        'productos': productos
    }
    return render(request, 'tienda/mantenedor_productos.html', contexto)

# --- Vistas de Categorías ---
def accion(request):
    # 1. Filtramos solo los juegos que pertenecen a la categoría "Acción"
    # (Asegúrate de que el nombre coincida exactamente con como lo escribiste en Oracle)
    lista_productos = Producto.objects.filter(categoria__nombre='Acción').order_by('id')
    
    # 2. Configuramos el Paginador (mostrar solo 4 juegos por página para probar)
    paginator = Paginator(lista_productos, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # 3. Enviamos los productos paginados a tu HTML
    contexto = {
        'productos': page_obj 
    }
    return render(request, 'tienda/categorias/accion.html', contexto) # Ajusta el nombre de tu html

def aventura(request):
    # 1. Filtramos solo los juegos que pertenecen a la categoría "Aventura"
    lista_productos = Producto.objects.filter(categoria__nombre='Aventura').order_by('id')
    
    # 2. Configuramos el Paginador
    paginator = Paginator(lista_productos, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 3. Enviamos los productos paginados a tu HTML
    contexto = {
        'productos': page_obj
    }
    return render(request, 'tienda/categorias/aventura.html', contexto)

def estrategia(request):
    # 1. Filtramos solo los juegos que pertenecen a la categoría "Estrategia"
    lista_productos = Producto.objects.filter(categoria__nombre='Estrategia').order_by('id')
    
    # 2. Configuramos el Paginador
    paginator = Paginator(lista_productos, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 3. Enviamos los productos paginados a tu HTML
    contexto = {
        'productos': page_obj
    }
    return render(request, 'tienda/categorias/estrategia.html', contexto)

def supervivencia(request):
    # 1. Filtramos solo los juegos que pertenecen a la categoría "Supervivencia"
    lista_productos = Producto.objects.filter(categoria__nombre='Supervivencia').order_by('id')
    
    # 2. Configuramos el Paginador
    paginator = Paginator(lista_productos, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 3. Enviamos los productos paginados a tu HTML
    contexto = {
        'productos': page_obj
    }
    return render(request, 'tienda/categorias/supervivencia.html', contexto)

def disparos(request):
    # 1. Filtramos solo los juegos que pertenecen a la categoría "Disparos"
    lista_productos = Producto.objects.filter(categoria__nombre='Disparos').order_by('id')
    
    # 2. Configuramos el Paginador
    paginator = Paginator(lista_productos, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 3. Enviamos los productos paginados a tu HTML
    contexto = {
        'productos': page_obj
    }
    return render(request, 'tienda/categorias/disparos.html', contexto)


# --- Función para Cerrar Sesión ---
def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('index')

# --- FUNCIÓN PARA ELIMINAR ---
@login_required(login_url='login')
def eliminar_producto(request, id):
    if not request.user.is_staff:
        return redirect('index')
        
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, '¡Producto eliminado correctamente!')
    return redirect('mantenedor')

# --- FUNCIÓN PARA EDITAR ---
@login_required(login_url='login')
def editar_producto(request, id):
    if not request.user.is_staff:
        return redirect('index')
        
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre_prod')
        producto.precio = request.POST.get('precio_prod')
        producto.stock = request.POST.get('stock_prod')
        
        # Actualizamos la categoría
        cat_id = request.POST.get('categoria_prod')
        producto.categoria = Categoria.objects.get(id=cat_id)
        
        # Solo actualizamos la imagen si el administrador subió una nueva
        if request.FILES.get('imagen_prod'):
            producto.imagen = request.FILES.get('imagen_prod')
            
        producto.save()
        messages.success(request, '¡Producto actualizado con éxito!')
        return redirect('mantenedor')

    contexto = {'producto': producto, 'categorias': categorias}
    return render(request, 'tienda/editar_producto.html', contexto)