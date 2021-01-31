import discord
from discord.ext import commands

class Messages(commands.Cog):

    def __init__(self, client):
        self.client = client

#Events
    

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('IRON'):
            response = 'Asta da frate, feru\'-i fer.'
            await message.channel.send(response)
        if message.content.startswith('BRONZE'):
            response = 'Măcar nu ești în divizie cu the Fer master.'
            await message.channel.send(response)
        if message.content.startswith('GOLD'):
            response = 'Fratelemeleu că mi-ar fi rușine să fiu Gold în sezonu\' ăsta'
            await message.channel.send(response)
        if message.content.startswith('PLATINUM'):
            response = 'Bă ăsta îi bun... Platina e fer greu frate'
            await message.channel.send(response)
        if message.content.startswith('DIAMOND'):
            response = 'Toate diamantele n-are valoarea ta.'
            await message.channel.send(response)
        if message.content.startswith('MASTER'):
            response = 'Tu și Maistoru\'' 
            await message.channel.send(response)
        if message.content.startswith('GRANDMASTER'):
            response = 'Tryhard.' 
            await message.channel.send(response)
        if message.content.startswith('CHALLENGER'):
            response = 'mă lași mă? iar ai cumpărat conturi?' 
            await message.channel.send(response)
        if message.content.startswith('Esti unranked'):
            response = 'UNRANKED?!?!? 我的妈呀，你这么菜吗???' 
            await message.channel.send(response)
    

#Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(Messages(client))