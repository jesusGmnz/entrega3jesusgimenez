from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    
class Productos(models.Model):
    tipo=models.CharField(max_length=40)
    aroma=models.CharField(max_length=40)
    precio=models.IntegerField()

class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    rut=models.IntegerField()
    email=models.EmailField()
    
class Envios(models.Model):
    direccion=models.CharField(max_length=40)
    fechaDeEnvio=models.DateField()
    enviado=models.BooleanField()