import os
import discord
from discord.ext import commands


TOKEN = os.environ["WIPE_TOKEN"]

intents = discord.Intents.default()
#client = discord.Client(intents=intents)

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot en línea')

@client.event
async def on_message(message):
    if message.content.startswith('!hola'):
        print("El comando está listo para recibir !hola")
        await message.channel.send('¡Hola!')
        print("El comando debe enviar '¡Hola!'")

client.run(TOKEN)
