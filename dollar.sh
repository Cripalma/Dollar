#!/bin/bash
echo "Eliminando contenido del docker"
docker stop dollar || true
docker rm -f dollar || true
docker rmi dollar:latest || true
echo "Creando la imagen docker"
docker build -t dollar .
echo "Ejecucion del conetendor"
docker run -d -p 8000:8000 --name dollar dollar:latest
echo "Contenedor operando"
docker ps