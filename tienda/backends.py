from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q

class EmailOUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Le decimos a Django: Busca un usuario cuyo username o cuyo email coincidan con lo que escribió
            usuario = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            
            # Si lo encuentra, verificamos la contraseña
            if usuario.check_password(password):
                return usuario
        except User.DoesNotExist:
            return None