import os
import math
import requests
from discord import Embed
from dotenv import load_dotenv
from discord.ext import commands
from helpers.to_string_helper import player_to_string, city_to_string

from argsparser import UserError
from helpers.parsers import playersParser

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='~')

@bot.command(name='player')
async def getPlayerByName(ctx, name): 
    print(f"user asked for command playerName with the paramter name={name} I will ask for name={name.lower()}")
    name = name.lower()
    url= f"http://localhost:9000/player?name={name}"
    try:
        player = requests.get(url)
        player.raise_for_status()        
    except requests.HTTPError as err:
        if err.response.status_code == 404:
            await ctx.send(f"user {name} wasn't found")
        else:
            await ctx.send(f"name: {name} error: {err}")
    else:
        allyId = player.json()['allyId']
        allyName = ""
        if allyId != "0": 
            try:            
                ally = requests.get(f"http://localhost:9000/ally?id={allyId}")
                ally.raise_for_status()
                allyName = ally.json()['allyName']
            except requests.HTTPError as err:
                if err.response.status_code == 404:
                    await ctx.send(f"ally {allyId} wasn't found")
                else:
                    await ctx.send(f"id: {allyId} error: {err}")    
            
        await ctx.send(player_to_string(player.json(), allyName))
        await print_cities_summary(ctx, player)           
@bot.command(name='playerId')
async def getPlayerById(ctx, id): 
    print(f"user asked for command playerId with the paramter id={id}")
    url= f"http://localhost:9000/player?id={id}"       
    try:
        player = requests.get(url) 
        player.raise_for_status()
    except requests.HTTPError as err:
        if err.response.status_code == 404:
            await ctx.send(f"user {id} wasn't found")
        else:
            await ctx.send(f"id: {id} error: {err}")
    else:
        allyId = player.json()['allyId']
        allyName = ""
        if allyId != 0: 
            try:            
                ally = requests.get(f"http://localhost:9000/ally?id={allyId}")
                ally.raise_for_status()
                allyName = ally.json()['allyName']
            except requests.HTTPError as err:
                if err.response.status_code == 404:
                    await ctx.send(f"ally {allyId} wasn't found")
                else:
                    await ctx.send(f"id: {allyId} error: {err}")    
            
        await ctx.send(player_to_string(player.json(), allyName))
        await print_cities_summary(ctx, player)  

@bot.command(name="players")
async def filterPlayers(ctx, *args):
    print(f"user asked for command players with the paramters {' '.join(args)}")
    try:
        (opts, _) = playersParser.parse(*args)
    except UserError as err:
        await ctx.send(f"players: {err.message}")
        # TODO: Send help embed.
        return
    if not opts: # If the dictionary is empty.
        await ctx.send("players: Please specify arguments to choose players by.")
        # TODO: Send help embed.
        return
    params = ""
    ally = None

    if "ally" in opts:
        ally = opts["ally"][0]
        params += f"allyName={ally}"
    
    url = f"http://localhost:9000/players?{params}"
    try:
        players = requests.get(url)
        players.raise_for_status()
    except requests.HTTPError as err:
        if err.response.status_code == 404:
            await ctx.send(f"players: Alliance `{ally}` wasn't found")
        else:
            await ctx.send(f"players: {err}")
        return
    
    sortedPlayers = players.json()["players"]
    #default sort
    sortedPlayers.sort(key = lambda player: int(player["place"]))

    embed = Embed(title=ally)
    part = 1
    total = int(math.ceil(len(sortedPlayers) / 25))
    fields = 0
    for player in sortedPlayers:
        desc = player_to_string(player, ally)
        embed.add_field(name=player["playerName"], value=desc, inline=False)
        fields += 1
        if fields == 25: # Embed is full
            embed.title = f"{ally} {part}\\{total}"
            await ctx.send(embed=embed)
            part += 1
            embed = Embed(title=f"{ally}  {part}\\{total}")
            fields = 0
    if fields > 0:
        await ctx.send(embed=embed)

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
            cities_str += "------------\n"
            cities_str += city_to_string(city)            
        await ctx.send(cities_str)

bot.run(TOKEN)


