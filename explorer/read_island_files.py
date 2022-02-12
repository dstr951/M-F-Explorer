import csv
import sys
import json
import asyncio
import datetime
import os
sys.path.append('../')
from helpers.html2json import reassembleIsland
from API.allies.postAllies import postAllies
from API.cities.postCities import postCities
from API.players.postPlayers import postPlayers
from API.islands.postIsland import postIsland
from dotenv import load_dotenv

load_dotenv()
ISLAND_FILES_PATH = os.getenv('ISLAND_FILES_PATH')

"""
maxInt = sys.maxsize
while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
"""



def postFile(island_html):        
    island_json, cities_json, players_json, allies_json = reassembleIsland(island_html)       
    
    postAllies(allies_json)
    postIsland(island_json)
    postCities(cities_json)
    postPlayers(players_json)
        
    
print(f"start in read_island_files, time is: {datetime.datetime.now()}")

        
for i in range (1, 5721):
    if i % 1000 == 1:
        print(i)
    current_file = open(f"{ISLAND_FILES_PATH}island_{i}.txt", 'r', encoding="utf-8") 
    current_text = current_file.read()
    postFile(current_text)


print(f"finish in read_island_files, time is: {datetime.datetime.now()}")  
