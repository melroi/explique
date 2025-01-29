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
        response = "explique hahaha pff ouais c'est un peu chiant les gars en gros Luden c'est un mythique qui donne de la péné magique et donc en en gros ça donne 6 de péné magique flat donc à 2 items complets.. donc il a 10 de péné flat donc il monte à 16, il a les bottes ça fait 18. Donc 16+18 ça fait 34 si jdis pas de conneries donc 34 + il avait shadow flame donc il a 44 et il a 44 et après du coup le void staff faut faire 44 divisé par 0.6 en gros il fait des dégats purs à un mec jusqu'à 73 d'rm j'avais dit 70 dans le cast à peu près et en gros bah les mecs ils ont pas 70 d'rm parce que globalement y'a eu un patch, en gros y'a le patch qui fait 0.8 d'rm sur les carrys et en gros de base sur lol y'avait pas ça et en gros la botlane va jamais prendre de la rm en lane en tout cas pas beaucoup donc c'est pas ouf en vrai j'pense que son item est nul donc en vrai j'pense soit il enlève shadow flame soit le void staff mais j'pense qu'il vaut mieux enlever shadow flame"
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
