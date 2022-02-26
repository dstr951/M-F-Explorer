from connect.session import *
from config import *
from random import randint
from helpers.html2json import getIsland
import time
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
ISLAND_FILES_PATH = os.getenv('ISLAND_FILES_PATH')

def start():
    home = 'USERPROFILE' if isWindows else 'HOME'
    os.chdir(os.getenv(home))
    if not os.path.isfile(ikaFile):
        open(ikaFile, 'w')
        os.chmod(ikaFile, 0o600)
    session = Session()
    
    
    for i in range(1, max_island + 1):        
        url = str(island_url + str(i))   
        resultValid = False
        while not resultValid:            
            html_data = session.get(url)              
            if html_data.find("error") == -1:                
                resultValid = True

        target_file = open(f"{ISLAND_FILES_PATH}/island_{i}.txt", 'w', encoding="utf-8")
        target_file.write(html_data)
        target_file.close()
        time.sleep(randint(5,15))   
    

print(f"start in main, time is: {datetime.datetime.now()}")
start()
print(f"finish in main, time is: {datetime.datetime.now()}")