from django.shortcuts import render

def index(request):
    # Esta función toma la petición del usuario y le devuelve el archivo index.html
    return render(request, 'tienda/index.html')