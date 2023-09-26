from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return render(request, "Aplicacion/inicio.html")

def vendedor(request):
    return render(request, "Aplicacion/vendedor.html")

def producto(request):
    return render(request, "Aplicacion/producto.html")

def cliente(request):
    return render(request, "Aplicacion/cliente.html")

def envios(request):
    return render(request, "Aplicacion/envios.html")

def Nuevo_Vendedor(resquest):
    return render(resquest, "Aplicacion/nuevo_vendedor.html")