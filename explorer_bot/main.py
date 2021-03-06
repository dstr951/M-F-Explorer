import os
import math
import string
import requests
from discord import Embed
from dotenv import load_dotenv
from discord.ext import commands
from helpers.to_string_helper import player_to_string, city_to_string

from argsparser import UserError, ArgsParser
from helpers.parsers import playersParser, playerParser

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='~')

@bot.command(name='player')
async def filterPlayer(ctx, *args):  
    print(f"user asked for command player with the paramters {' '.join(args)}")
    emptyErrorMsg = False
    (opts, _) = await parseArgs(ctx, playerParser, "player", emptyErrorMsg, *args)
    # exit from the function if opts returned as boolean    
    if type(opts) == type(True):
        return
    if len(_) == 0:
        await ctx.send(f"no username was sepcified")
    name = _[0]
    strippedName = name.strip("|")    
    params = f"name={strippedName}"
    print(f"user asked for command playerName with the paramter name={name} I will ask for name={strippedName}")
    url= f"http://localhost:9000/player?{params}"
    try:
        player = requests.get(url)
        player.raise_for_status()        
    except requests.HTTPError as err:
        if err.response.status_code == 404:
            await ctx.send(f"user {name} wasn't found")
            return
        else:
            await ctx.send(f"name: {name} error: {err}")
            return
    
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
    minimal = False
    if opts:
        if "minimal" in opts:
            minimal = True
    await print_cities_summary(ctx, player, minimal)           
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
    emptyErrorMsg = "Please specify arguments to choose players by."
    (opts, _) = await parseArgs(ctx, playersParser, "players", emptyErrorMsg, *args)
    #if parseArgs return False
    if not opts:
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
    sortedPlayers.sort(key = lambda player: int(player["place"] if player["place"] != '' else "0"))

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

async def print_cities_summary(ctx, player, minimal = False):
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
        cities_str=f"???????? ????????: {len(cities_list)}\n"
        for city in cities_list:
            if not minimal:
                cities_str += "------------\n"
            cities_str += city_to_string(city, minimal)            
        await ctx.send(cities_str)

async def parseArgs(ctx, parser:ArgsParser, commandName, emptyErrorMsg, *args):
    try:
        (opts, _) = parser.parse(*args)
    except UserError as err:
        await ctx.send(f"{commandName}: {err.message}")
        # TODO: Send help embed.
        return (False, False)
    if emptyErrorMsg is string:
        if not opts: # If the dictionary is empty.
            await ctx.send(f"{commandName}: {emptyErrorMsg}")
            # TODO: Send help embed.
            return (False, False)
    return (opts, _)

bot.run(TOKEN)


