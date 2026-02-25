# models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"