import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "explique":
        await message.channel.send("explique hahaha pff ouais c'est un peu chiant les gars en gros Luden c'est un mythique qui donne de la péné magique et donc en en gros ça donne 6 de péné magique flat donc à 2 items complets.. donc il a 10 de péné flat donc il monte à 16, il a les bottes ça fait 18. Donc 16+18 ça fait 34 si jdis pas de conneries donc 34 + il avait shadow flame donc il a 44 et il a 44 et après du coup le void staff faut faire 44 divisé par 0.6 en gros il fait des dégats purs à un mec jusqu'à 73 d'rm j'avais dit 70 dans le cast à peu près et en gros bah les mecs ils ont pas 70 d'rm parce que globalement y'a eu un patch, en gros y'a le patch qui fait 0.8 d'rm sur les carrys et en gros de base sur lol y'avait pas ça et en gros la botlane va jamais prendre de la rm en lane en tout cas pas beaucoup donc c'est pas ouf en vrai j'pense que son item est nul donc en vrai j'pense soit il enlève shadow flame soit le void staff mais j'pense qu'il vaut mieux enlever shadow flame")
        print("sent")
    await bot.process_commands(message)

TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
