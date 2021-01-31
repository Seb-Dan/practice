import discord
import time
import asyncio
from discord.ext import commands

class Sounds(commands.Cog):

    def __init__(self, client):
        self.client = client

# Events
#     @commands.Cog.listener()
#     async def on_ready(self):
#         print('Bot is online.')

#Commands

    @commands.command()
    async def hi(self, ctx):
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

    @commands.command()
    async def felina(self, ctx):
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

        vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/felina.mp3'))
        await asyncio.sleep(5)
        await ctx.message.delete()
        # await vc.disconnect()

    @commands.command()
    async def laba(self, ctx):
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

    @commands.command()
    async def badumts(self, ctx):
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

        vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/badumts.mp3'))
        await asyncio.sleep(5)
        await ctx.message.delete()
        # await vc.disconnect()
    
    @commands.command()
    async def cunosc(self, ctx):
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

        vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/cunosc.mp3'))
        await asyncio.sleep(5)
        await ctx.message.delete()
        # await vc.disconnect()

    @commands.command()
    async def DIAMOND(self, ctx):
        
        channel = None

        if ctx.author.voice is None or ctx.author.voice.channel is None:
            return
        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            vc = await voice_channel.connect()

        else:
            await ctx.voice_client.move_to(voice_channel)
            vc = ctx.voice_client

        vc.play(discord.FFmpegPCMAudio(executable='E:/ffmpeg/bin/ffmpeg.exe', source = 'E:/audios/audios for rank/diamant.mp3'))
        await asyncio.sleep(5)
        await ctx.message.delete()
        # await vc.disconnect()    

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(client):
    client.add_cog(Sounds(client))