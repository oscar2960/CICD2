================================================================================
PROYECTO DE SOFTWARE BASADO EN HERRAMIENTAS DE INTEGRACIÓN CONTINUA
================================================================================

NOMBRE: Oscar Andres Ortiz Barrera
INSTITUCIÓN: Politécnico Grancolombiano
MÓDULO: Énfasis Profesional I (Integración Continua)
ENTREGA: Semana 3 - Construcción e Intercomunicación de Contenedores Docker

--------------------------------------------------------------------------------
1. DESCRIPCIÓN DEL PROYECTO
--------------------------------------------------------------------------------
Este repositorio contiene la solución técnica para la Entrega 1 (Semana 3) del 
proyecto grupal de Integración Continua. 

El objetivo principal de esta fase es implementar Docker como herramienta 
fundamental de infraestructura para construir dos contenedores independientes 
que logren comunicarse entre sí a través de una red interna.

La arquitectura elegida para demostrar esta comunicación consta de:
- Contenedor A: Una base de datos relacional (PostgreSQL).
- Contenedor B: Una aplicación backend (Python) que verifica la conexión activa.

--------------------------------------------------------------------------------
2. ARQUITECTURA Y TECNOLOGÍAS UTILIZADAS
--------------------------------------------------------------------------------
- Docker: Para la creación y aislamiento de los entornos (contenedores).
- Docker Compose: Para la orquestación, gestión de variables de entorno y 
  creación de la red compartida entre los servicios.
- Python 3.9 (Alpine/Slim): Lenguaje base para el script de prueba de conexión.
- PostgreSQL 13 (Alpine): Motor de base de datos SQL.
- Psycopg2: Adaptador de base de datos PostgreSQL para el lenguaje Python.

--------------------------------------------------------------------------------
3. ESTRUCTURA DE ARCHIVOS
--------------------------------------------------------------------------------
/
|-- app.py               # Lógica de conexión a la base de datos.
|-- requirements.txt     # Dependencias de Python (psycopg2).
|-- Dockerfile           # Instrucciones de construcción de la imagen Python.
|-- docker-compose.yml   # Configuración de servicios, puertos y redes.
|-- README.txt           # Documentación y especificaciones del proyecto.

--------------------------------------------------------------------------------
4. INSTRUCCIONES DE EJECUCIÓN (PASO A PASO)
--------------------------------------------------------------------------------
Para ejecutar este proyecto en cualquier entorno local, asegúrate de tener 
instalado Docker y Docker Compose.

Paso 1: Clonar el repositorio.
$ git clone <URL_DEL_REPOSITORIO>
$ cd <NOMBRE_DE_LA_CARPETA>

Paso 2: Construir y levantar los contenedores.
Ejecuta el siguiente comando en la raíz del proyecto (donde se ubica el 
archivo docker-compose.yml):
$ docker-compose up --build

Paso 3: Verificación de resultados.
En la consola, observarás el proceso de descarga de imágenes y construcción.
Una vez levantados los servicios, la terminal mostrará los logs combinados. 
Busca la siguiente salida generada por el contenedor de la aplicación Python:

"Intentando conectar a la base de datos en el host 'db'..."
"¡Éxito! La aplicación Python y la base de datos PostgreSQL se están 
comunicando correctamente."

Paso 4: Detener los contenedores.
Para apagar la infraestructura de manera segura y limpiar la red, utiliza:
$ docker-compose down

--------------------------------------------------------------------------------
5. JUSTIFICACIÓN TÉCNICA
--------------------------------------------------------------------------------
- Se utilizó la directiva 'depends_on' en el docker-compose.yml para asegurar 
  que el contenedor de la aplicación no intente iniciar hasta que el contenedor 
  de la base de datos esté en proceso de arranque.
- El script 'app.py' incluye un mecanismo de reintentos (retries). Esto es una 
  buena práctica en entornos DevOps, ya que PostgreSQL tarda unos segundos en 
  estar listo para aceptar conexiones, incluso si su contenedor ya está activo.
- Se utilizaron variables de entorno (environment) para pasar credenciales, 
  evitando codificar contraseñas de forma rígida en el código fuente (Hardcoding).