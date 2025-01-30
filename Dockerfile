# Utiliser une image Python légère
FROM python:3.11-slim

# Installer les bibliothèques système nécessaires
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libasound2 \
    libpulse0 \
    libaudio2 \
    libxext6 \
    libxrender1 \
    libsm6 \
    libice6 \
    && rm -rf /var/lib/apt/lists/*

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copier tout le code du projet
COPY . .

# Exécuter le bot
CMD ["python", "bot.py"]
