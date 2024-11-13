# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de la aplicación al contenedor
COPY calculator.py /app/calculator.py

# Instala CherryPy
RUN pip install cherrypy

# Expone el puerto en el que correrá CherryPy
EXPOSE 8080

# Ejecuta la aplicación CherryPy
CMD ["python", "calculator.py"]
