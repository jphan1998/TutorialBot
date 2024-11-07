import discord
from discord.app_commands import guilds
from discord.ext import commands
from typing import Final
import os
from dotenv import load_dotenv

#Load your private discord token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Create an instance of a client
intents = discord.Intents.all()
client = commands.Bot(command_prefix='@', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def server(ctx):
    await ctx.send(ctx.guild)

@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('bye'):
        await message.channel.send('Goodbye!')
    await client.process_commands(message)



# Run the bot
client.run(token=TOKEN)