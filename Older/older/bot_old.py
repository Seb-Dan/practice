import os
import random
import discord
import asyncio
import youtube_dl
import time
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print('Bot online.')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def helpme(ctx):
    #In this case you have to use the ctx to send the message
    #Good to remember that ctx is NOT a parameter wich the user will give
    msg = f'Hi {ctx.author.mention}, here are some useful commands.\r\n $join,\r\n $leave,\r\n $hi,\r\n $nu,\r\n $david,\r\n $cunosc'
    await ctx.send(msg)

@bot.event
async def on_message(message):

    if message.content == 'GOLD':
        response = 'Fratelemeleu că mi-ar fi rușine să fiu Gold în Sezonu\' ăsta'
        await message.channel.send(response)

@bot.event
async def on_message(message):

    if message.content == 'PLATINUM':
        response = 'Bă ăsta îi bun... Platina e fer greu frate'
        await message.channel.send(response)

@bot.command()
async def hi(ctx):
        # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        vc = await voice_channel.connect()

    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/Hi.mp3'))
    await asyncio.sleep(5)
    await ctx.message.delete()
    # await vc.disconnect()

@bot.command()
async def nu(ctx):
        # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        vc = await voice_channel.connect()
        
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/Nu.mp3'))
    await asyncio.sleep(5)
    await ctx.message.delete()
    # await vc.disconnect()

@bot.command()
async def cunosc(ctx):
        # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        vc = await voice_channel.connect()
        
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/Cunostinta.mp3'))
    await asyncio.sleep(5)
    await ctx.message.delete()
    # await vc.disconnect()

@bot.command()
async def david(ctx):
        # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        vc = await voice_channel.connect()
        
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/david-crop.mp3'))
    await asyncio.sleep(5)
    await ctx.message.delete()
    # await vc.disconnect()

@bot.command()
async def laba(ctx):
        # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        vc = await voice_channel.connect()
        
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/laba.mp3'))
    await asyncio.sleep(5)
    await ctx.message.delete()
    # await vc.disconnect()

@bot.command()
async def iuhuhui(ctx):
        # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        vc = await voice_channel.connect()
        
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/iuhuhui.mp3'))
    await asyncio.sleep(5)
    await ctx.message.delete()
    # await vc.disconnect()

@bot.command()
async def haha(ctx):
        # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        vc = await voice_channel.connect()
        
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/haha.mp3'))
    await asyncio.sleep(5)
    await ctx.message.delete()
    # await vc.disconnect()

bot.run(TOKEN)