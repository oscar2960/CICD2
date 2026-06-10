pipeline {
    // Ejecutar en cualquier nodo disponible que tenga Docker instalado
    agent any

    environment {
        // Asignar un nombre de proyecto único para evitar conflictos si hay múltiples ejecuciones
        COMPOSE_PROJECT_NAME = "proyecto_ic_${env.BUILD_ID}"
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                echo "Descargando el código fuente desde el repositorio..."
                checkout scm
            }
        }

        stage('Construir Imágenes Docker') {
            steps {
                echo "Construyendo los contenedores de Base de Datos y Aplicación..."
                // Actualizado a Docker Compose V2 (sin guion)
                sh 'docker compose build'
            }
        }

        stage('Prueba de Integración (Ejecución)') {
            steps {
                echo "Levantando servicios y verificando comunicación..."
                // Actualizado a Docker Compose V2 (sin guion)
                sh 'docker compose up --abort-on-container-exit'
            }
        }
    }

    post {
        always {
            echo "Limpiando el entorno y eliminando contenedores..."
            // Esta línea se mantiene comentada para que puedas tomar tus evidencias visuales.
            // Una vez tomes la captura de 'docker ps', quita las '//' para futuras ejecuciones.
            sh 'docker compose down -v'
        }
        success {
            echo "¡Integración Continua exitosa! Los contenedores se comunicaron correctamente."
        }
        failure {
            echo "Fallo en la integración. Revisa los logs para identificar el problema."
        }
    }
}
