import discord
import os
import json
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)

status = cycle(['League of Legends', 'Pornhub Superstars', 'Mario 3D'])

# @client.event
# async def on_ready():
#     await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hey there nerds.'))
#     change_status.start()
#     print('Bot is online.')



@tasks.loop(seconds=360)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    change_status.start()
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild: \n' 
        f'{guild.name} (id: {guild.id})'
    )

    for guild in client.guilds:
        for member in guild.members:
            print(member.name, ' ')

    members = '\n - '.join([member.name for member in guild.members])
    return(f'Guild Members:\n - {members}')

client.run(TOKEN)