from django.urls import path
from Aplicacion import views



urlpatterns = [
    
    path('inicio', views.inicio, name="Inicio"),
    path('vendedor',views.vendedor, name="Vendedor"),
    path('productos',views.producto, name="Productos"),
    path('cliente',views.cliente, name="Cliente"),
    path('envios',views.envios, name="Envios"),
    path('Nuevo_vendedor', views.Nuevo_Vendedor)
    
]
