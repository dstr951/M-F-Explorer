from connect.session import *
from config import *
from random import randint
from helpers.html2json import getIsland
import time
import json
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
ISLAND_FILES_PATH = os.getenv('ISLAND_FILES_PATH')
ISLAND_JSON_PATH = os.getenv('ISLAND_JSON_PATH')
MAIL1 = os.getenv("MAIL_1")
PASSWORD1 = os.getenv("PASSWORD_1")
MAIL2 = os.getenv("MAIL_2")
PASSWORD2 = os.getenv("PASSWORD_2")
MAIL3 = os.getenv("MAIL_3")
PASSWORD3 = os.getenv("PASSWORD_3")

def start():
    home = 'USERPROFILE' if isWindows else 'HOME'
    os.chdir(os.getenv(home))
    if not os.path.isfile(ikaFile):
        open(ikaFile, 'w')
        os.chmod(ikaFile, 0o600)
    sessions = []
    sessions.append(Session(MAIL1, PASSWORD1))
    time.sleep(2)
    sessions.append(Session(MAIL2, PASSWORD2))
    time.sleep(2)
    #sessions.append(Session(MAIL3, PASSWORD3))
    max_sessions = len(sessions)

    islands_file = open(f"{ISLAND_JSON_PATH}/islands_list.json")
    islands = json.load(islands_file)
    session_num = 0
    for island in islands:
        islandId = island['island_id']
        url = str(island_url + str(islandId))   
        resultValid = False
        while not resultValid:            
            html_data = sessions[session_num].get(url)              
            if html_data.find("gf_vhost_not_found") == -1:                
                resultValid = True

        target_file = open(f"{ISLAND_FILES_PATH}/island_{islandId}.txt", 'w', encoding="utf-8")
        target_file.write(html_data)
        target_file.close()
        session_num += 1
        if session_num >= max_sessions: session_num = 0
        time.sleep(random.random() + 0.5)    

print(f"start in main, time is: {datetime.datetime.now()}")
start()
print(f"finish in main, time is: {datetime.datetime.now()}")