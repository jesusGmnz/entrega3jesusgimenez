from django.urls import path
from .views import *



urlpatterns = [
    
    path('inicio',inicio, name="Inicio"),
    path('vendedor',vendedor, name="Vendedor"),
    path('productos',producto, name="Productos"),
    path('cliente',cliente, name="Cliente"),
    path('envios',envios, name="Envios"),
    path('crearVendedor',crearVendedor, name="crearVendedor"),
    path('agregarProducto',agregarProducto, name="agregarProducto"),
    path('registroCliente',registroCliente, name="registroCliente" ),
    path('agendarEnvio',agendarEnvio, name="agendarEnvio"),
    path('buscarCliente',buscarCliente, name="buscarCliente"),
    path('resultadoCliente',resultadoCliente, name="resultadoCliente"),
    path('borrarVendedor/<vendedor_nombre>/', eliminarVendedor, name="borrarVendedor"),
    path('borrarCliente/<cliente_nombre>/', eliminarCliente, name="borrarCliente"),
    path('editarCliente/<cliente_nombre>/', actualizarCliente, name='editarCliente'),
    
]
