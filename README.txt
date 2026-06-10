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
Este repositorio contiene la solución técnica y de infraestructura para las 
entregas de las Semanas 3 y 5 del proyecto grupal de Integración Continua (CI).

El sistema consta de una arquitectura backend multi-contenedor automatizada mediante 
un pipeline de operaciones que valida de forma continua la correcta construcción, 
despliegue e intercomunicación de los servicios.

Componentes principales:
- Servidor de Base de Datos: Motor relacional SQL basado en PostgreSQL.
- Aplicación de Verificación: Script en Python que valida la disponibilidad y 
  conectividad de la base de datos en red.
- Servidor de Automatización: Orquestador Jenkins que gestiona el ciclo de vida 
  del código (Clonación, Construcción, Pruebas Integradas y Limpieza).

--------------------------------------------------------------------------------
2. ARQUITECTURA Y TECNOLOGÍAS UTILIZADAS
--------------------------------------------------------------------------------
- Docker: Para el aislamiento de entornos en contenedores independientes.
- Docker Compose: Para la definición de la infraestructura como código (IaC), 
  gestión de variables de entorno y establecimiento de la red interna compartida.
- Jenkins: Gestor y motor de operaciones para el Pipeline de Integración Continua.
- Python 3.9-slim: Imagen base optimizada para la ejecución de la app de pruebas.
- PostgreSQL 13-alpine: Imagen ligera para el motor de base de datos SQL.
- Psycopg2-binary: Adaptador de red para la conexión Python-PostgreSQL.

--------------------------------------------------------------------------------
3. ESTRUCTURA DE ARCHIVOS DEL REPOSITORIO
--------------------------------------------------------------------------------
/
|-- app.py               # Script de lógica de red y reintentos de conexión.
|-- requirements.txt     # Definición de dependencias de software (psycopg2).
|-- Dockerfile           # Instrucciones de compilación para el entorno Python.
|-- docker-compose.yml   # Orquestador de contenedores, puertos y redes.
|-- Jenkinsfile          # Tubería declarativa (Pipeline) para la automatización CI.
|-- README.txt           # Guía de especificaciones y documentación general (v2).

--------------------------------------------------------------------------------
4. CONFIGURACIÓN E IMPLEMENTACIÓN DE JENKINS (PASO A PASO)
--------------------------------------------------------------------------------
Para desplegar este pipeline en tu entorno de Jenkins, sigue detalladamente los 
siguientes pasos operacionales:

Paso 1: Desbloqueo Inicial de Jenkins
Al levantar Jenkins por primera vez, el sistema solicitará una contraseña de 
administrador. Esta se puede recuperar de dos maneras:
- Revisando los registros de la consola (logs), ubicando la línea bajo el texto:
  "Please use the following password to proceed to installation".
- Consultando directamente el archivo del sistema en la ruta:
  `/var/jenkins_home/secrets/initialAdminPassword`
Introduce dicha clave alfanumérica en el navegador para desbloquear la plataforma.

Paso 2: Instalación de Complementos (Plugins)
- Selecciona "Instalar complementos sugeridos" (Install suggested plugins).
- Una vez dentro del panel de control, dirígete a: Administrar Jenkins -> 
  Administrar Plugins -> Pestaña "Disponibles" e instala los siguientes:
  * Docker Pipeline
  * Docker plugin
  Esto facultará a Jenkins para interpretar y ejecutar comandos de Docker en los scripts.

Paso 3: Creación y Vinculación del Pipeline (Job)
1. En el panel principal, haz clic en "Nueva Tarea" (New Item).
2. Asigna un nombre descriptivo (ej. 'Proyecto-Integracion-Continua') y elige la 
   opción "Pipeline". Haz clic en OK.
3. Desplázate hasta la sección inferior de "Pipeline" y configura:
   - Definition: Selecciona "Pipeline script from SCM".
   - SCM: Selecciona "Git".
   - Repository URL: Pega el enlace HTTPS de tu repositorio de GitHub.
   - Branch Specifier: Asegúrate de apuntar a la rama correcta (ej. '*/main').
   - Script Path: Confirma que apunta exactamente a 'Jenkinsfile'.
4. Haz clic en Guardar (Save).

--------------------------------------------------------------------------------
5. CONTROL DE EJECUCIÓN Y CAPTURA DE REFERENCIAS VISUALES
--------------------------------------------------------------------------------
El pipeline declarativo está diseñado bajo la filosofía DevOps de "entornos 
efímeros", lo que significa que levanta los contenedores, realiza las pruebas de 
intercomunicación, y al finalizar con éxito ("success") ejecuta un bloque post-action 
con `docker-compose down -v` para limpiar el servidor y liberar memoria.
