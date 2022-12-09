# Descargamos la imagen necesaria de fastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi

# Instalamos las librerias necesarias para el proyecto
RUN pip install pandas

RUN pip install requests

# Abrimos el puerto 80 mediante la cual se va a comunicar nuestra API
EXPOSE 80

# Copiamos los archivos del proyecto al contenedor de Docker. El . antes de /app indica la ruta absoluta de la carpeta app
COPY ./app /app
