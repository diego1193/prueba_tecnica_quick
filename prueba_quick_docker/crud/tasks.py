from celery import shared_task
from django.http import HttpResponse
import csv
import os
from django.conf import settings
from .models import Client, Bill 
from io import StringIO

@shared_task
def procesar_archivo_csv(data):
    f = StringIO(data)
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        document, first_name, last_name, email = row
        Client.objects.create(document=document, first_name=first_name, last_name=last_name, email=email)

    return "Clientes cargados"



@shared_task
def generate_csv():
    base_dir = settings.MEDIA_ROOT
    filename = 'clientes.csv'
    file_path = os.path.join(base_dir, filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w', newline='') as csvfile:  # Utiliza file_path aquí
        fieldnames = ['documento', 'nombre_completo', 'cantidad_facturas']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for cliente in Client.objects.all():
            writer.writerow({
                'documento': cliente.document,
                'nombre_completo': f"{cliente.first_name} {cliente.last_name}",
                'cantidad_facturas': Bill.objects.filter(client_id=cliente).count()
            })

    return file_path

