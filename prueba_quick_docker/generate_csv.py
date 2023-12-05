import csv
import os

# Ruta del proyecto (modificar según sea necesario)
ruta_proyecto = '/home/diego/Documents/prueba_tecnica_quick/'  # Reemplaza con la ruta real de tu proyecto

# Nombre del archivo CSV
nombre_archivo = 'usuarios_prueba.csv'
ruta_archivo = os.path.join(ruta_proyecto, nombre_archivo)

# Datos de ejemplo para 10 usuarios
usuarios = [
    ['1234567890', 'Juan', 'Pérez', 'juan.perez@example.com'],
    ['1234567891', 'Ana', 'Gómez', 'ana.gomez@example.com'],
    ['1234567892', 'Luis', 'Martínez', 'luis.martinez@example.com'],
    ['1234567893', 'Laura', 'López', 'laura.lopez@example.com'],
    ['1234567894', 'Carlos', 'Hernández', 'carlos.hernandez@example.com'],
    ['1234567895', 'Sofía', 'García', 'sofia.garcia@example.com'],
    ['1234567896', 'Diego', 'Álvarez', 'diego.alvarez@example.com'],
    ['1234567897', 'Lucía', 'Fernández', 'lucia.fernandez@example.com'],
    ['1234567898', 'David', 'Sánchez', 'david.sanchez@example.com'],
    ['1234567899', 'María', 'Rodríguez', 'maria.rodriguez@example.com']
]

# Crear y escribir en el archivo CSV
with open(ruta_archivo, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['document', 'first_name', 'last_name', 'email'])
    writer.writerows(usuarios)

print(f"Archivo CSV creado en {ruta_archivo}")
