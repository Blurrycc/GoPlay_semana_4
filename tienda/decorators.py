from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps

def requiere_rol_admin(view_func):
    """
    Decorador que verifica si el usuario autenticado tiene el Rol de 'Administrador'.
    Si no lo tiene, lanza un error 403 (Permiso Denegado).
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # 1. Si el usuario ni siquiera ha iniciado sesión, lo mandamos al login
        if not request.user.is_authenticated:
            return redirect('login') 
        
        # 2. Verificamos su rol a través del PerfilUsuario
        try:
            # Buscamos el nombre del rol asociado a este usuario (ignorando mayúsculas/minúsculas)
            nombre_rol = request.user.perfilusuario.rol.nombre.lower()
            
            if nombre_rol == 'administrador' or nombre_rol == 'admin':
                # Si es administrador, lo dejamos pasar a la vista
                return view_func(request, *args, **kwargs)
                
        except Exception:
            # Si el usuario no tiene PerfilUsuario o no tiene Rol asignado, capturamos el error
            pass 
        
        # 3. Si llega a este punto, significa que inició sesión pero NO es administrador.
        # Lanzamos un error de Permiso Denegado (Pantalla 403)
        raise PermissionDenied

    return _wrapped_view