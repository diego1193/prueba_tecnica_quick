# Prueba Técnica: Sistema de Gestión CRUD 📖

## Descripción

En esta prueba técnica, se desarrolla un sistema de gestión para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en diversas entidades: Clientes, Facturas y Productos. El proyecto se estructura en torno al siguiente diagrama de entidad-relación:

![Diagrama de Entidad-Relación](/imagenes_readme/img1.jpeg)

## Características Principales

### Autenticación y Seguridad

- **Registro de Usuarios**: Se implementa un endpoint para registrar usuarios, solicitando correo electrónico y contraseña.
- **Inicio de Sesión y JWT**: Un endpoint de inicio de sesión valida las credenciales del usuario y, en caso de éxito, genera un JSON Web Token (JWT). Este token es esencial para asegurar el acceso a los endpoints del sistema, validando las solicitudes a través de la cabecera de autenticación.

### Operaciones CRUD

Las siguientes entidades están disponibles para operaciones CRUD a través de la API:

- **Clientes**
- **Facturas**
- **Productos**
- **Facturas y Productos**

### Endpoints Adicionales

- **Generación de CSV Asíncrona**: Endpoint permite la generación de un archivo CSV exportable de manera asíncrona. Este archivo incluye una lista de todos los clientes junto con campos específicos requeridos.
- **Cargue Masivo de Clientes**: Endpoint facilita el cargue masivo asíncrono de clientes a través de un archivo CSV.

## Uso y Documentación 📋

### Desarrollo y Tecnologías Implementadas

Este proyecto ha sido desarrollado utilizando el framework Django junto con Django REST Framework, siguiendo el patrón de arquitectura Modelo-Vista-Controlador (MVC). Se han implementado diversos endpoints para manejar las operaciones requeridas, proporcionando una API robusta y segura. 

Para la autenticación y seguridad, se ha integrado JSON Web Token (JWT) asegurando así la protección de los endpoints. La elección de SQLite como sistema de gestión de base de datos ofrece una solución ligera y eficiente para el almacenamiento de datos. Además, para manejar operaciones asíncronas, se ha empleado Celery con Redis, lo que mejora significativamente el rendimiento de las tareas en segundo plano.

En cuanto al despliegue, se ha optado por Docker y Docker Compose, facilitando la contenerización y la gestión de la aplicación y sus dependencias de manera eficiente y escalable.

### Librerías y Herramientas Utilizadas

- **Django**: Un framework web de alto nivel para el desarrollo rápido y limpio del backend, fomentando un diseño pragmático y limpio.
- **Django REST Framework**: Potente y flexible framework para construir APIs RESTful, mejorando la funcionalidad de Django con un conjunto de herramientas adicionales para la creación de APIs.
- **Celery**: Una solución asíncrona robusta, utilizada para manejar tareas en segundo plano y operaciones que requieren un alto rendimiento sin bloquear el hilo principal de ejecución.
- **SQLite**: Sistema de gestión de bases de datos relacional ligero, que ofrece un almacenamiento de datos sencillo y efectivo para aplicaciones de menor escala.
- **Docker**: Plataforma de contenerización que permite empaquetar y ejecutar aplicaciones en un entorno aislado llamado contenedor, facilitando el despliegue y la escalabilidad.
- **Redis**: Almacenamiento en estructura de datos en memoria, utilizado como base de datos, caché y broker de mensajes, complementando a Celery en la gestión de tareas asíncronas.


## Configuración y Despliegue 🛠️

### Requisitos Previos

Antes de comenzar, asegúrate de tener instalados **Docker** y **Docker Compose** en tu sistema. Estas herramientas son esenciales para construir y ejecutar el entorno contenerizado del proyecto. Además, para facilitar las pruebas de los endpoints, puedes unirte al siguiente workspace de Postman, que es de acceso público:

[Workspace de Postman](https://app.getpostman.com/join-team?invite_code=f6fe94c368956d7061029e348d7eb8b7&target_code=bbb9099bcfa6c47b14afdb2b48a10ac)

### Clonar el Repositorio

Para obtener una copia del proyecto, clónalo en la carpeta de tu elección utilizando el siguiente comando:

```bash
git clone https://github.com/diego1193/prueba_tecnica_quick.git
```
### Ejecución del Programa

Después de clonar el repositorio, encontrarás una carpeta llamada `prueba_tecnica_quick`. Abre una terminal en tu ordenador y navega a esta carpeta. Dentro de ella, ingresa a la subcarpeta `prueba_quick_docker`, donde se encuentran los archivos de Docker.

Ejecuta los siguientes comandos para construir y levantar los servicios del proyecto:

```cmd
docker-compose build
docker-compose up
```

Estos comandos construirán el entorno necesario y pondrán en marcha el proyecto. Una vez completado, estarás listo para empezar a probar los endpoints y realizar operaciones CRUD a través de la API.

## Prueba Endpoints 🚀

Una vez levantado el proyecto podemos ingresar al admin de django con la siguiente url:

```
http://localhost:8000/admin/
``` 

El usuario y contrasena son los siguientes

```
Usuario: root@quick.com
Password: root
``` 
Luego empezar con el registro y validaciones soportando este [Workspace de Postman](https://app.getpostman.com/join-team?invite_code=f6fe94c368956d7061029e348d7eb8b7&target_code=bbb9099bcfa6c47b14afdb2b48a10ac).

### Registro de Usuario

Para registrar un nuevo usuario, envía una petición POST a la siguiente URL:

```
http://localhost:8000/registro/
``` 

Incluye en la petición un JSON con los datos del usuario. Por ejemplo:

```json
{
  "nombre": "Juan Perez",
  "correo": "juanperez@example.com",
  "contrasena": "password123"
}
``` 
Si el registro es exitoso, recibirás un código de estado HTTP 201 y los detalles del usuario recién creado.

Ejemplo de respuesta:

 ![Img 1](/imagenes_readme/img2.jpeg)

 ### Login de Usuario

Para iniciar sesión, envía una petición POST a la siguiente URL:

```
http://localhost:8000/login/
``` 

Incluye las credenciales del usuario en el cuerpo de la petición en formato JSON. Por ejemplo:

```json
{
  "correo": "juan@example.com",
  "contrasena": "password123"
}
``` 
Una respuesta exitosa devolverá un código de estado HTTP 201 y un JSON con dos tokens: refresh y access. El token refresh se utiliza para obtener un nuevo token access cuando sea necesario, mientras que el token access se usa como JSON Web Token para autenticar las solicitudes a los endpoints protegidos.
 
Ejemplo de respuesta:

 ![Img 2](/imagenes_readme/img3.jpeg)

### Agregando JWT a los Endpoints

Para probar los endpoints protegidos en Postman, necesitarás incluir el JSON Web Token (JWT) obtenido después del inicio de sesión. Si estás utilizando el [Workspace de Postman](https://app.getpostman.com/join-team?invite_code=f6fe94c368956d7061029e348d7eb8b7&target_code=bbb9099bcfa6c47b14afdb2b48a10ac), puedes configurar el token como una variable global de entorno.

#### Configuración del Token:

1. **Obtener el Token**: Inicia sesión mediante el endpoint de login para obtener el `access token`.

    Ejemplo de token obtenido:
    
    ![Imagen del Token](/imagenes_readme/img4.jpeg)

2. **Agregar el Token al Entorno Global**:
   
    En Postman, ve a la sección de "Environments" y configura una nueva variable global llamada `token` con el valor del JWT.

    Cómo agregar el token:
    
    ![Agregar Token al Entorno Global](/imagenes_readme/img5.jpeg)

#### Uso del Token en las Solicitudes:

- Al realizar solicitudes a endpoints protegidos, asegúrate de incluir el token JWT en la cabecera `Authorization` con el prefijo `Bearer`.
- Puedes hacerlo automáticamente en Postman seleccionando `Bearer Token` en el tipo de autorización y utilizando la variable global previamente configurada.

Siguiendo estos pasos, podrás probar fácilmente los endpoints protegidos de tu API en Postman.

---

### CRUD de Entidades

Las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) están disponibles para las siguientes entidades: Clientes, Productos y Facturas. A continuación, se detallan los endpoints y ejemplos para cada entidad.

#### Instrucciones Generales

- Para todas las operaciones CRUD, asegúrate de incluir el token JWT en la cabecera `Authorization` de tu petición.
- Las peticiones POST y PUT deben incluir un cuerpo en formato JSON con los datos relevantes.
- Las respuestas incluirán un código de estado HTTP y, en algunos casos, datos adicionales o confirmación de la acción realizada.

---

### CRUD Clientes

- **GET `http://127.0.0.1:8000/clients/`**: Obtiene todos los clientes.
- **POST `http://127.0.0.1:8000/clients/`**: Crea un nuevo cliente.
- **PUT `http://127.0.0.1:8000/clients/{id}/`**: Actualiza un cliente existente.
- **DELETE `http://127.0.0.1:8000/clients/{id}/`**: Elimina un cliente.

Ejemplo de petición POST y PUT para crear un cliente:

```json
{
  "document": "12347",
  "first_name": "Juan",
  "last_name": "Melo",
  "email": "juan.melo2@example.com"
}
```
 ---
 ### CRUD Productos

- **GET `http://127.0.0.1:8000/products/`**: Obtiene todos los producto.
- **POST `http://127.0.0.1:8000/products/`**: Crea un nuevo producto.
- **PUT `http://127.0.0.1:8000/products/{id}/`**: Actualiza un producto existente.
- **DELETE `http://127.0.0.1:8000/products/{id}/`**: Elimina un producto.

Ejemplo de petición POST y PUT para crear un producto:

```json
{
  "name": "Producto 2",
  "description": "Descripción del Producto Ejemplo"
}
```
 ---
 ### CRUD Facturas

- **GET `http://127.0.0.1:8000/bills/`**: Obtiene todos las factura.
- **POST `http://127.0.0.1:8000/bills/`**: Crea una nueva factura.
- **PUT `http://127.0.0.1:8000/bills/{id}/`**: Actualiza una factura existente.
- **DELETE `http://127.0.0.1:8000/bills/{id}/`**: Elimina una factura.

Ejemplo de petición POST y PUT para crear una factura:

```json
{
  "client_id": 1, // Asegúrate de que este ID exista en tu base de datos
  "company_name": "Gufy 1 S.A.S",
  "nit": 1234562,
  "code": "Factura003"
}
```
---
 ### CRUD Factura Producto

- **GET `http://127.0.0.1:8000/billproducts/`**: Obtiene todos las facturas producto.
- **POST `http://127.0.0.1:8000/billproducts/`**: Crea una nueva facturas producto.
- **PUT `http://127.0.0.1:8000/billproducts/{id}/`**: Actualiza una facturas producto.
- **DELETE `http://127.0.0.1:8000/billproducts/{id}/`**: Elimina una facturas producto.

Ejemplo de petición POST y PUT para crear una facturas producto.:

```json
{
  "client_id": 1, // Asegúrate de que este ID exista en tu base de datos
  "company_name": "Gufy 1 S.A.S",
  "nit": 1234562,
  "code": "Factura003"
}
```
---
### Endpoints para Manejo de CSV

Para utilizar estos endpoints, es necesario incluir el JSON Web Token (JWT) en la cabecera de autorización.

#### Generación de CSV

- **GET `http://localhost:8000/generate-csv/`**: Inicia la generación de un archivo CSV de forma asíncrona. Este archivo incluye los nombres completos de los clientes, su documento y el número de facturas asociadas a cada cliente.

    Ejemplo de respuesta al iniciar la generación del CSV:

    ```json
    {
        "message": "Generación de CSV iniciada",
        "task_id": "850291b9-5fb0-4f4a-8688-91fce9cd55b6"
    }
    ```
---
#### Consulta del Estado del CSV


- **GET `http://localhost:8000/get-csv-status/{task_id}/`**:  Consulta el estado de la generación del CSV. Reemplaza {task_id} con el ID de tarea obtenido en la generación del CSV.

    Ejemplo de respuesta:

    ```json
    {
        "status": "Completado",
        "ruta": "clientes.csv"
    }
    ```
---

#### Descarga del CSV


- **GET `http://localhost:8000/descargar-csv/`**:  Descarga el archivo CSV generado.

    Ejemplo de contenido del CSV:

    ```
    documento,nombre_completo,cantidad_facturas
    12347,Juan Melo,0
    ```

---
#### Cargue Masivo de Clientes


- **POST `http://localhost:8000/cargar-clientes/`**: Permite el cargue masivo de clientes mediante la subida de un archivo CSV.

    Sigue este formato para la carga del archivo:

    ![Imagen SUBIR CSV](/imagenes_readme/IMG1.jpeg)

    Puedes descargar el archivo `usuarios_prueba.csv` como plantilla para facilitar el proceso de carga masiva de clientes.