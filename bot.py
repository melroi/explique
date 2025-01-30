import discord
import os
import sys
from discord.ext import commands
from discord import FFmpegPCMAudio
from playsound import playsound  # Importer playsound

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    """S'exécute quand le bot est connecté et prêt."""
    print(f"[LOG] Bot connecté en tant que {bot.user} et prêt à fonctionner")

@bot.command()
async def join(ctx):
    """Rejoint le canal vocal de l'utilisateur."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        print(f"[LOG] Bot rejoint le canal vocal: {channel.name}")
    else:
        await ctx.send("Tu dois être dans un canal vocal pour utiliser cette commande!")
        print("[LOG] Tentative de rejoindre un canal vocal échouée: utilisateur non connecté")

@bot.command()
async def leave(ctx):
    """Quitte le canal vocal."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        print("[LOG] Bot quitte le canal vocal")
    else:
        await ctx.send("Je ne suis pas dans un canal vocal!")
        print("[LOG] Tentative de quitter un canal vocal échouée: bot non connecté")

@bot.command()
async def play(ctx):
    """Joue le fichier audio."""
    if ctx.voice_client:
        try:
            # Utiliser FFmpeg pour jouer le fichier audio dans le canal vocal
            source = FFmpegPCMAudio('fichier.mp3')
            ctx.voice_client.play(source)
            print("[LOG] Lecture du fichier audio démarrée")
        except Exception as e:
            await ctx.send("Erreur lors de la lecture du fichier audio!")
            print(f"[LOG] Erreur de lecture audio: {str(e)}")
    else:
        await ctx.send("Je dois être dans un canal vocal pour jouer de l'audio!")
        print("[LOG] Tentative de lecture audio échouée: bot non connecté")

@bot.command()
async def play_local(ctx):
    """Joue un fichier audio local (non dans le canal vocal)."""
    try:
        playsound('fichier.mp3')  # Joue le fichier audio localement
        print("[LOG] Lecture du fichier audio local démarrée")
    except Exception as e:
        print(f"[LOG] Erreur de lecture audio locale: {str(e)}")

@bot.event
async def on_message(message):
    """Réagit aux messages reçus."""
    if message.author == bot.user:
        return

    print(f"[LOG] Message reçu de {message.author}: {message.content}") 

    explique_variants = ["explique", "expliques", "expliquer", "expliquez", "expliqué", "expliquée", "expliqués", "expliquées"]

    if any(variant in message.content.lower() for variant in explique_variants):
        response = "explique hahaha pff ouais c'est un peu chiant les gars en gros Luden c'est un mythique qui donne de la péné magique et donc en en gros ça donne 6 de péné magique flat donc à 2 items complets.. donc il a 10 de péné flat donc il monte à 16, il a les bottes ça fait 18. Donc 16+18 ça fait 34 si jdis pas de conneries donc 34 + il avait shadow flame donc il a 44 et il a 44 et après du coup le void staff faut faire 44 divisé par 0.6 en gros il fait des dégats purs à un mec jusqu'à 73 d'rm j'avais dit 70 dans le cast à peu près et en gros bah les mecs ils ont pas 70 d'rm parce que globalement y'a eu un patch, en gros y'a le patch qui fait 0.8 d'rm sur les carrys et en gros de base sur lol y'avait pas ça et en gros la botlane va jamais prendre de la rm en lane en tout cas pas
