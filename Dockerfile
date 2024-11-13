# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos y la aplicación al contenedor
COPY app.py /app/app.py

# Instala CherryPy
RUN pip install cherrypy

# Expone el puerto en el que correrá CherryPy
EXPOSE 8080

# Ejecuta la aplicación CherryPy
CMD ["python", "app.py"]
