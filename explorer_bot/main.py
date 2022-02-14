

import os
import requests
from dotenv import load_dotenv
from discord.ext import commands
from helpers.to_string_helper import player_to_string, city_to_string

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='~')

@bot.command(name='playerName')
async def getPlayerByName(ctx, name): 
    print(f"user asked for command playerName with the paramter name={name}")
    url= f"http://localhost:9000/players?name={name}"
    try:
        player = requests.get(url)
        player.raise_for_status()
    except requests.HTTPError as err:
        if err.response.status_code == 404:
            await ctx.send(f"user {name} wasn't found")
        else:
            await ctx.send(f"name: {name} error: {err}")
    else:
        await ctx.send(player_to_string(player.json()))
        print_cities_summary(ctx, player)           
@bot.command(name='playerId')
async def getPlayerByName(ctx, id): 
    print(f"user asked for command playerId with the paramter id={id}")
    url= f"http://localhost:9000/players?id={id}"       
    try:
        player = requests.get(url) 
        player.raise_for_status()
    except requests.HTTPError as err:
        if err.response.status_code == 404:
            await ctx.send(f"user {id} wasn't found")
        else:
            await ctx.send(f"id: {id} error: {err}")
    else:
        await ctx.send(player_to_string(player.json()))
        print_cities_summary(ctx, player)

async def print_cities_summary(ctx, player):
    playerId = player.json()['playerId']
    url= f"http://localhost:9000/cities?playerId={playerId}"
    try:
        cities = requests.get(url)
        cities.raise_for_status()
    except requests.HTTPError as err:
        if err.response.status_code == 400:
            await ctx.send(f"bad request")
        else:
            await ctx.send(f"playerId: {playerId} error: {err}")
    else:            
        cities_list = cities.json()["cities"]
        await ctx.send(f"מספר ערים:{len(cities_list)}")
        cities_str=""
        for city in cities_list:
            cities_str += city_to_string(city)
        await ctx.send(cities_str)

bot.run(TOKEN)


