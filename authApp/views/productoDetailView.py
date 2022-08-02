from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authApp.models.productos import Producto
from authApp.serializers.productosSerializer import ProductosSerializer

class ProductoDetailView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer


    def get(self, request, *args, **kwargs):
        return super().get(request,*args,**kwargs)