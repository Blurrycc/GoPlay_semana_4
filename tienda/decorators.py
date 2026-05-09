from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps

def requiere_rol_admin(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') 
        
        # 1. Intentamos obtener el rol de forma segura
        try:
            nombre_rol = request.user.perfilusuario.rol.nombre.lower()
        except Exception:
            nombre_rol = None 
        
        # 2. Evaluamos los permisos FUERA del try/except
        # Así, si la vista tiene un error (como un HTML faltante), Django nos mostrará el error real.
        if nombre_rol == 'administrador' or nombre_rol == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return _wrapped_view