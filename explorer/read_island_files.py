import os
import sys
import json
import datetime
sys.path.append('../')
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from helpers.html2json import reassembleIsland
from API.allies.postAllies import postAllies
from API.cities.postCities import postCities
from API.players.postPlayers import postPlayers
from API.islands.postIsland import postIsland
from requests.packages.urllib3.util.retry import Retry

load_dotenv()
ISLAND_FILES_PATH = os.getenv('ISLAND_FILES_PATH')
ISLAND_JSON_PATH = os.getenv('ISLAND_JSON_PATH')

def postFile(island_html):        
    island_json, cities_json, players_json, allies_json = reassembleIsland(island_html)       
    
    postAllies(allies_json)
    postIsland(island_json)
    postCities(cities_json)
    postPlayers(players_json)
        
    
print(f"start in read_island_files, time is: {datetime.datetime.now()}")
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
        
islands_file = open(f"{ISLAND_JSON_PATH}/islands_list.json")
islands = json.load(islands_file)
session_num = 0
for island in islands:
    islandId = island['island_id']
    try:
        current_file = open(os.path.join(f"{ISLAND_FILES_PATH}/island_{islandId}.txt"), 'r', encoding="utf-8") 
        current_text = current_file.read()
        postFile(current_text)
    except FileNotFoundError:
        print(f"file: {ISLAND_FILES_PATH}/island_{islandId}.txt not found")
    finally:
        current_file.close()
    


print(f"finish in read_island_files, time is: {datetime.datetime.now()}")  
