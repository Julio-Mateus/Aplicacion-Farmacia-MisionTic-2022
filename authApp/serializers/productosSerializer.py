from authApp.models.productos import Producto
from rest_framework import serializers

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields =['id_producto', 'nombre_producto', 'categoria_producto','cant_disponible']
    
    def to_representation(self, obj): # Serializacion objeto Python a JSON
        producto = Producto.objects.get(id_producto = obj.id_producto)
        return {
            'id_producto':producto.id_producto,
            'nombre_producto': producto.nombre_producto,
            'categoria_producto': producto.categoria_producto,
            'cant_disponible': producto.cant_disponible,
        }
