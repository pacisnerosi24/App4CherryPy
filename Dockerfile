# Usa la imagen base de Python 3.11.10
FROM python:3.11.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de código de la aplicación al contenedor
COPY . /app

# Instala CherryPy
RUN pip install cherrypy

# Expone el puerto 8080 (puerto por defecto de CherryPy)
EXPOSE 8080

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
