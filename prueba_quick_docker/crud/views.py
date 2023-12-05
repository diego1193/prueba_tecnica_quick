from rest_framework import viewsets, status
from django.http import HttpResponse
from django.conf import settings
from django.http import Http404
import os
from .models import Client, Bill, Product, BillProduct
from .serializers import ClientSerializer, BillSerializer, ProductSerializer, BillProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.response import Response
from .tasks import generate_csv, procesar_archivo_csv

from celery.result import AsyncResult

from rest_framework.parsers import MultiPartParser


@api_view(['POST'])
@parser_classes([MultiPartParser])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def cargar_clientes(request):
    if 'archivo' in request.FILES:
        archivo = request.FILES['archivo']
        task = procesar_archivo_csv.delay(archivo.read().decode('utf-8'))
        return Response({"message": "Carga iniciada", "task_id": task.id})
    return Response({"message": "No se proporcionó un archivo"}, status=400)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def start_csv_generation(request):
    task = generate_csv.delay() 
    return Response({"message": "Generación de CSV iniciada", "task_id": task.id})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_csv_status(request, task_id):
    task_result = AsyncResult(task_id)
    if task_result.ready():
        ruta_archivo = task_result.result 
        return Response({"status": "Completado", "ruta": ruta_archivo})
    else:
        return Response({"status": "En proceso"})

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def descargar_csv(request):
    filename = 'clientes.csv'
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse("Archivo no encontrado", status=404)

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

