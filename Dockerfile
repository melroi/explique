# Utiliser l'image officielle Python
FROM python:3.11

# Installer ffmpeg et les bibliothèques nécessaires
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libglib2.0-0 \
    libasound2 \
    libpulse0 \
    libaudio2 \
    libxext6 \
    libxrender1 \
    libsm6 \
    libice6 \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier requirements.txt et installer les dépendances Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . /app

# Exposer le port si nécessaire
EXPOSE 8080

# Lancer l'application
CMD ["python", "bot.py"]
