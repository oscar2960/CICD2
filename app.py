import os
import time
import psycopg2

# Las credenciales y host se inyectan dinámicamente desde docker-compose
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_NAME = os.environ.get('DB_NAME', 'postgres')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASS = os.environ.get('DB_PASSWORD', 'password')

def connect_to_db():
    retries = 5
    while retries > 0:
        try:
            print(f"Intentando conectar a la base de datos en el host '{DB_HOST}'...")
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            print("¡Éxito! La aplicación Python y la base de datos PostgreSQL se están comunicando correctamente.")
            conn.close()
            return
        except psycopg2.Error as e:
            print(f"Fallo en la conexión: {e}. Reintentando en 3 segundos... ({retries} intentos restantes)")
            retries -= 1
            time.sleep(3)
    print("Error crítico: No se pudo establecer la conexión a la base de datos después de varios intentos.")

if __name__ == "__main__":
    connect_to_db()