import discord
import os
import sys
import speech_recognition as sr
import subprocess
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

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
    """Rejoint le canal vocal de l'utilisateur et commence à écouter."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        print(f"[LOG] Bot rejoint le canal vocal: {channel.name}")
        await ctx.send("🎤 J'écoute les voix...")

        # Commence l'écoute
        await listen_voice(ctx, vc)
    else:
        await ctx.send("Tu dois être dans un canal vocal pour utiliser cette commande!")
        print("[LOG] Tentative échouée : utilisateur non connecté")

@bot.command()
async def leave(ctx):
    """Quitte le canal vocal."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        print("[LOG] Bot quitte le canal vocal")
    else:
        await ctx.send("Je ne suis pas dans un canal vocal!")
        print("[LOG] Tentative échouée : bot non connecté")

async def listen_voice(ctx, vc):
    """Écoute et analyse les voix en temps réel."""
    recognizer = sr.Recognizer()
    
    while vc.is_connected():
        with sr.Microphone() as source:
            try:
                print("[LOG] Écoute en cours...")
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio, language="fr-FR")
                print(f"[LOG] Transcription : {text}")

                # Détection de mots-clés
                explique_variants = ["explique", "expliques", "expliquer", "expliquez"]
                if any(word in text.lower() for word in explique_variants):
                    response = "explique hahaha pff ouais c'est un peu chiant les gars en gros Luden..."
                    await ctx.send(response)
                    print(f"[LOG] Réponse envoyée : {response[:50]}...")

            except sr.UnknownValueError:
                print("[LOG] Impossible de reconnaître l'audio")
            except sr.RequestError:
                print("[LOG] Erreur avec l'API de reconnaissance vocale")

@bot.event
async def on_disconnect():
    """Log lorsque le bot se déconnecte."""
    print("[LOG] Bot déconnecté")

@bot.event
async def on_error(event, *args, **kwargs):
    """Log les erreurs."""
    print(f"[LOG] Erreur détectée dans {event}: {sys.exc_info()[1]}")

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    print("[LOG] Démarrage du bot...")
    bot.run(TOKEN)
else:
    print("[LOG] ERREUR : Le token Discord est introuvable ! Vérifie tes variables d'environnement.")
