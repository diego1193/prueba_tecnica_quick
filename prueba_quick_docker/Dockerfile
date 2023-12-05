# Usar una imagen oficial de Python como imagen base
FROM python:3.10

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requerimientos y instalar las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente de la aplicación
COPY . /app/

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000
