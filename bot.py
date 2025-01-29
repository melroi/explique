import discord
import os
import sys
from discord.ext import commands

# Création du bot avec tous les intents activés
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    """S'exécute quand le bot est connecté et prêt."""
    print(f"[LOG] Bot connecté en tant que {bot.user} et prêt à fonctionner")

@bot.event
async def on_message(message):
    """Réagit aux messages reçus."""
    if message.author == bot.user:
        return  # Ignore les messages du bot lui-même

    print(f"[LOG] Message reçu de {message.author}: {message.content}")  # Log le message reçu

    if message.content.lower() == "explique":
        response = "Explique hahaha pff ouais c'est un peu chiant les gars en gros Luden..."
        await message.channel.send(response)
        print(f"[LOG] Réponse envoyée dans #{message.channel}: {response[:50]}...")  # Log la réponse

    await bot.process_commands(message)  # Permet aux autres commandes de fonctionner

@bot.event
async def on_disconnect():
    """Log lorsque le bot se déconnecte."""
    print("[LOG] Bot déconnecté")

@bot.event
async def on_error(event, *args, **kwargs):
    """Log les erreurs."""
    print(f"[LOG] Erreur détectée dans {event}: {sys.exc_info()[1]}")

# Récupération du token d'environnement et lancement du bot
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN:
    print("[LOG] Démarrage du bot...")
    bot.run(TOKEN)
else:
    print("[LOG] ERREUR : Le token Discord est introuvable ! Vérifie tes variables d'environnement.")
