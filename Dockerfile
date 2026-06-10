# Usar una imagen oficial de Python en su versión ligera
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script principal de la aplicación
COPY app.py .

# Ejecutar el script al iniciar el contenedor
CMD ["python", "app.py"]