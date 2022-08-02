from django.db import models

class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre_producto = models.CharField('NomProd', max_length=255, default="")
    categoria_producto = models.CharField('Categoria', max_length=255, default="")
    cant_disponible = models.BigIntegerField(default=1)