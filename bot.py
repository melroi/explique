import discord
import os
import sys
from discord.ext import commands
from discord import FFmpegPCMAudio  # Utilisation de FFmpeg pour lire l'audio
import subprocess  # Pour vérifier si FFmpeg est installé

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    """S'exécute quand le bot est connecté et prêt."""
    print(f"[LOG] Bot connecté en tant que {bot.user} et prêt à fonctionner")

    # Vérification si FFmpeg est installé
    try:
        subprocess.run(["ffmpeg", "-version"], check=True)
        print("[LOG] FFmpeg est installé et fonctionne.")
    except Exception as e:
        print(f"[LOG] Erreur : FFmpeg n'est pas installé ! {e}")

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
async def play(ctx, url=None):
    """Joue un fichier audio ou un lien YouTube."""
    if ctx.voice_client:
        try:
            # Vérifier si une URL est fournie, sinon jouer un fichier local
            if url:
                audio_source = FFmpegPCMAudio(url)
            else:
                audio_source = FFmpegPCMAudio('fichier.mp3')  # Remplacez par le bon fichier

            ctx.voice_client.play(audio_source)
            await ctx.send("Lecture audio en cours...")
            print("[LOG] Lecture du fichier audio démarrée")
        except Exception as e:
            await ctx.send("Erreur lors de la lecture du fichier audio!")
            print(f"[LOG] Erreur de lecture audio: {str(e)}")
    else:
        await ctx.send("Je dois être dans un canal vocal pour jouer de l'audio!")
        print("[LOG] Tentative de lecture audio échouée: bot non connecté")

@bot.event
async def on_message(message):
    """Réagit aux messages reçus."""
    if message.author == bot.user:
        return

    print(f"[LOG] Message reçu de {message.author}: {message.content}") 

    explique_variants = ["explique", "expliques", "expliquer", "expliquez", "expliqué", "expliquée", "expliqués", "expliquées"]

    if any(variant in message.content.lower() for variant in explique_variants):
        response = "explique hahaha pff ouais c'est un peu chiant les gars en gros Luden c'est un mythique qui donne de la péné magique..."
        await message.channel.send(response)
        print(f"[LOG] Réponse envoyée dans #{message.channel}: {response[:50]}...")  

    await bot.process_commands(message)  

@bot.event
async def on_disconnect():
    """Log lorsque le bot se déconnecte."""
    print("[LOG] Bot déconnecté")

@bot.event
async def on_error(event, *args, **kwargs):
    """Log les erreurs."""
    print(f"[LOG] Erreur détectée dans {event}: {sys.exc_info()[1]}")

TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN:
    print("[LOG] Démarrage du bot...")
    bot.run(TOKEN)
else:
    print("[LOG] ERREUR : Le token Discord est introuvable ! Vérifie tes variables d'environnement.")
