import discord
from discord.ext import commands
import os

# On active les intents nécessaires
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Liste des mots déclencheurs
trigger_words = ["explique", "expliques", "explik", "expliquer"]

# Variable pour garder une trace des connexions vocales
voice_clients = {}

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user.name}')

@bot.command(name='join')
async def join(ctx):
    """Commande pour faire rejoindre le bot dans ton canal vocal"""
    if not ctx.author.voice:
        await ctx.send("Tu dois être dans un canal vocal !")
        return
    
    channel = ctx.author.voice.channel
    try:
        voice_client = await channel.connect()
        voice_clients[ctx.guild.id] = voice_client
        await ctx.send(f"J'ai rejoint {channel.name}")
    except Exception as e:
        await ctx.send(f"Je n'ai pas pu rejoindre le canal: {str(e)}")

@bot.command(name='leave')
async def leave(ctx):
    """Commande pour faire partir le bot du canal vocal"""
    if ctx.guild.id in voice_clients:
        await voice_clients[ctx.guild.id].disconnect()
        del voice_clients[ctx.guild.id]
        await ctx.send("Je suis parti du canal vocal !")
    else:
        await ctx.send("Je ne suis pas dans un canal vocal !")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Vérifie si le message contient un mot déclencheur
    if any(word in message.content.lower() for word in trigger_words):
        # Envoie le message texte
        await message.channel.send("explique hahaha pff ouais c'est un peu chiant les gars...")
        
        # Si le bot est dans un canal vocal, joue le son
        if message.guild.id in voice_clients:
            voice_client = voice_clients[message.guild.id]
            if not voice_client.is_playing():
                try:
                    audio_source = discord.FFmpegPCMAudio('explique.mp3')
                    voice_client.play(audio_source)
                except Exception as e:
                    print(f"Erreur lors de la lecture audio: {e}")

    await bot.process_commands(message)

TOKEN = 'TON_TOKEN_ICI'  # Remplace par ton token
bot.run(TOKEN)