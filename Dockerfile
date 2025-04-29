FROM python:3.9-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    sqlite3 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Création du répertoire pour les données
RUN mkdir -p /data

# Copie des fichiers d'application
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Volume pour stocker la base de données SQLite
VOLUME ["/data"]

# Exposition du port
EXPOSE 5000

# Démarrage de l'application
CMD ["python", "app.py"]