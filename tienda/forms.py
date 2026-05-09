from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario, Rol


class PerfilUsuarioForm(forms.ModelForm):
    # Añadimos los campos de contraseña que no vienen por defecto en el modelo User
    password = forms.CharField(widget=forms.PasswordInput(), required=False, label="Nueva Contraseña")
    password_confirmacion = forms.CharField(widget=forms.PasswordInput(), required=False, label="Confirmar Contraseña")

    class Meta:
        model = User
        # Estos son los campos del usuario que permitiremos editar
        fields = ['first_name', 'last_name', 'email'] 

    # Validación estricta en el servidor 
    def clean(self):
        # Ejecutamos las validaciones normales primero
        cleaned_data = super().clean() 
        
        # Obtenemos las contraseñas que el usuario escribió
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirmacion")

        # Si el usuario intentó cambiar la contraseña, verificamos que coincidan
        if password or password_confirm:
            if password != password_confirm:
                # Si no coinciden, Django bloquea el guardado y lanza este error
                raise forms.ValidationError("Las contraseñas no coinciden. Por favor, verifica e inténtalo de nuevo.")
        
        return cleaned_data


class PerfilUsuarioAdminForm(forms.ModelForm):
    # Traemos todos los roles disponibles de la base de datos Oracle
    rol = forms.ModelChoiceField(
        queryset=Rol.objects.all(), 
        empty_label="Seleccione un Rol",
        widget=forms.Select(attrs={'class': 'form-select text-bg-dark border-secondary'})
    )

    class Meta:
        model = PerfilUsuario
        fields = ['rol', 'telefono', 'direccion']
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control text-bg-dark border-secondary'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control text-bg-dark border-secondary'}),
        }
