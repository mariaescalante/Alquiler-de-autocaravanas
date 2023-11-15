from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    unidades = models.IntegerField()

    def str(self):
        return self.nombre