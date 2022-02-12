import requests

def postPlayers(players_json):
    url = "http://localhost:9000/players"  
    data = {"players": players_json}  
    res = requests.post(url, json= data)  
    return res   

#leave for testing
#postPlayers([{"playerId": "30", "playerName": "Codename", "allyId": "1", "place": "19", "buildingScore": "10,227,413", "researchScore": "5,261,160", "armyScore": "104,600", "traderSecondaryScore": "3,377,620"}])