from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f"Cliente {self.nombre} {self.apellido} DNI: {self.dni}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    cuil = models.IntegerField()
    provincia = models.CharField(max_length=30)
    
    def __str__(self):
            return f"Proveedor {self.nombre} {self.cuil} {self.provincia}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    codigo = models.IntegerField()
    precio = models.FloatField()
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"Producto {self.nombre} {self.marca} {self.codigo} {self.precio} {self.cantidad}"