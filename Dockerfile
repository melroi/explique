# Utiliser l'image officielle Python
FROM python:3.11

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    ffmpeg \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier requirements.txt et installer les dépendances Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code du bot
COPY . /app

# Exposer le port si nécessaire
EXPOSE 8080

# Lancer le bot
CMD ["python", "bot.py"]
