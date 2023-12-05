from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import Http404
from .models import Client, Bill, Product, BillProduct
from .serializers import ClientSerializer, BillSerializer, ProductSerializer, BillProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class BaseViewSet(viewsets.ModelViewSet):
    """
    Clase base para ViewSets con comportamiento personalizado en la eliminación y recuperación.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            return Response({"mensaje": "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"mensaje": "Registro eliminado correctamente"}, status=status.HTTP_200_OK)
        except Http404:
            return Response({"mensaje": "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)


class ClientViewSet(BaseViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class BillViewSet(BaseViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BillProductViewSet(BaseViewSet):
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return super().create(request, *args, **kwargs)
        return Response({"mensaje": "Factura o producto, no existe"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return super().update(request, *args, **kwargs)
        return Response({"mensaje": "Factura o producto, no existe"}, status=status.HTTP_400_BAD_REQUEST)

