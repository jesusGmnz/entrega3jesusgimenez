from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def inicio(request):
    return render(request, "Aplicacion/inicio.html")


def vendedor(request):

    todos = Vendedor.objects.all()

    return render(request, "Aplicacion/vendedor.html", {"ven": todos})


def producto(request):
    return render(request, "Aplicacion/producto.html")


def cliente(request):
    
    todos = Cliente.objects.all()

    return render(request, "Aplicacion/cliente.html",{"cliente": todos})


def envios(request):
    return render(request, "Aplicacion/envios.html")


def crearVendedor(request):

    if request.method == 'POST':

        vendedor_nuevo = Vendedor(nombre=request.POST["nombre"], apellido=request.POST["apellido"])
        vendedor_nuevo.save()
        return render(request, "Aplicacion/inicio.html")

    return render(request, "Aplicacion/crear_vendedor.html")


def agregarProducto(request):

    if request.method == 'POST':

        nuevo_producto = Productos(
            tipo=request.POST['tipo'], aroma=request.POST['aroma'], precio=request.POST['precio'])
        nuevo_producto.save()
        return render(request, "Aplicacion/inicio.html")

    return render(request, "Aplicacion/agregar_producto.html")


def registroCliente(request):
    
    if request.method == "POST":
        
        miFormulario = ClienteFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            clienteNuevo = Cliente(nombre=informacion["nombre"], apellido=informacion["apellido"],rut=informacion["rut"],email=informacion["email"],)
            clienteNuevo.save()
            return render(request, "Aplicacion/inicio.html")
    else:
        miFormulario = ClienteFormulario()
        
    return render(request, "Aplicacion/registro_cliente.html", {"form": miFormulario})


def agendarEnvio(request):

    if request.method == 'POST':

        nuevo_envio = Envios(
            direccion=request.POST['direccion'], fechaDeEnvio=request.POST['fechaDeEnvio'], enviado=request.POST['enviado'])
        nuevo_envio.save()
        return render(request, "Aplicacion/inicio.html")

    return render(request, "Aplicacion/agendar_envio.html")


def buscarCliente(request):

    return render(request, "Aplicacion/buscar_cliente.html")


def resultadoCliente(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        clienteresultado = Cliente.objects.filter(nombre__icontains=nombre)

        return render(request, "Aplicacion/resultado_cliente.html", {"valor": nombre, "res": clienteresultado})
    else:
        return HttpResponse("No enviaste Datos.")

    return render(request, "Aplicacion/resultado_cliente.html")


def eliminarVendedor(request, vendedor_nombre):
    vendedorEliminado = Vendedor.objects.get(nombre=vendedor_nombre)
    vendedorEliminado.delete()
    todos = Vendedor.objects.all()

    return render(request, "Aplicacion/vendedor.html", {"ven": todos})

def eliminarCliente(request, cliente_nombre):
    clienteEliminado = Cliente.objects.get(nombre=cliente_nombre)
    clienteEliminado.delete()
    todos = Cliente.objects.all()

    return render(request, "Aplicacion/cliente.html", {"cliente": todos})

def actualizarCliente(request, cliente_nombre):
    
    clienteElegido = Cliente.objects.get(nombre=cliente_nombre)
    
    if request.method == "POST":
        
        miFormulario = ClienteFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            clienteElegido.nombre = informacion["nombre"]
            clienteElegido.apellido = informacion["apellido"]
            clienteElegido.rut = informacion["rut"]
            clienteElegido.email = informacion["email"]
            
            clienteElegido.save()
            
            return render(request, "Aplicacion/inicio.html")
    else:
        miFormulario = ClienteFormulario(initial={"nombre": clienteElegido.nombre,
                                                "apellido": clienteElegido.apellido,
                                                "rut": clienteElegido.rut,
                                                "email": clienteElegido.email})
        
    return render(request, "Aplicacion/registro_cliente.html", {"form": miFormulario})
