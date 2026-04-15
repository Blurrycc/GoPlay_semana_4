from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esto le dice a Django: "Cualquier ruta que llegue, mándala a las urls de la app tienda"
    path('', include('tienda.urls')), 
]