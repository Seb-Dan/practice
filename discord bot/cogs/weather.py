import requests
import discord
import asyncio
import json
import geopy
import os
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
from types import SimpleNamespace

APITOKEN = os.getenv('API_TOKEN')

class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def weather(self, ctx): 
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
        longi = "19.944544"
        lati = "50.049683"
        querystring = {"lon": longi,"lat": lati}

        headers = {
            'x-rapidapi-key': APITOKEN,
            'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)['data'][0]
        await ctx.send('In '+str(data['city_name'])+', the weather report is: '+str(data['weather']['description'])+', with a temperature of '+str(data['temp'])+'C. '+'Date: '+str(data['ob_time']))

        # print(json.dumps(data, sort_keys=True,
        # indent=4, separators=(',', ': ')))
        



def setup(client):
    client.add_cog(Weather(client))