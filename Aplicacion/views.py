from django.shortcuts import render
from django.http import HttpResponse
from .models import *


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

def crearVendedor(request):
    
    if request.method == 'POST':
        
        vendedor_nuevo = Vendedor(nombre = request.POST["nombre"], apellido = request.POST["apellido"])
        vendedor_nuevo.save()
        return render(request, "Aplicacion/inicio.html")
    
    
    return render(request, "Aplicacion/crear_vendedor.html")

def agregarProducto(request):
    
    if request.method == 'POST':
        
        nuevo_producto = Productos(tipo=request.POST['tipo'], aroma=request.POST['aroma'], precio=request.POST['precio'])
        nuevo_producto.save()
        return render(request, "Aplicacion/inicio.html")
    
    return render(request, "Aplicacion/agregar_producto.html")

def registroCliente(request):
    
    if request.method == 'POST':
        
        nuevo_cliente = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], rut=request.POST['rut'], email=request.POST['email'])
        nuevo_cliente.save()
        return render(request, "Aplicacion/inicio.html")
    
    return render(request, "Aplicacion/registro_cliente.html")

def agendarEnvio(request):
    
    if request.method == 'POST':
        
        nuevo_envio = Envios(direccion=request.POST['direccion'], fechaDeEnvio=request.POST['fechaDeEnvio'], enviado=request.POST['enviado'])
        nuevo_envio.save()
        return render(request, "Aplicacion/inicio.html")
    
    return render(request, "Aplicacion/agendar_envio.html")