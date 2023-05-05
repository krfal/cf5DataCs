FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Instala las dependencias
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libgomp1 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Copia el código y los archivos necesarios al contenedor
COPY . /app

# Ejecuta el comando por defecto para iniciar la aplicación
CMD ["python", "-u", "main.py"]
