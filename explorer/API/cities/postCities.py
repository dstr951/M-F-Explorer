import requests

def postCities(cities_json):
    url = "http://localhost:9000/cities"  
    data = {"cities": cities_json}  
    res = requests.post(url, json= data)   
    return res  

#leave for testing
#postCities([{"cityId": 30, "islandId": "1", "cityName": "שיש", "level": "18", "playerId": "30", "state": ""}, {"cityId": 6015, "islandId": "1", "cityName": "פוליס", "level": "3", "playerId": "97", "state": ""}, {"cityId": 1963, "islandId": "1", "cityName": "J-L Ponthy", "level": "16", "playerId": "101", "state": ""}, {"cityId": 38, "islandId": "1ordan", "level": "13", "playerId": "38", "state": ""}, {"cityId": 34, "islandId": "1", "cityName": "polis I", "level": "15", "playerId": "34", "state": ""}, {"cityId": 936, "islandId": "1", "cityName": "הקלע של יוני", "level": "24", "playerId": "604", "state": ""}, {"cityId": 407, "islandId": "1", "cityName": "שיש 2", "level": "16", "playerId": "68", "state": ""}, {"cityId": 39, "islandId": "1", "cityName": "פוליס", "level": "3", "playerId": "39", "state": ""}, {"cityId": 1290, "islandId": "1", "cityName": "הקלע של יוני", "level": "20", "playerId": "132", "state": ""}, {"cityId": 646, "islandId": "1", "cityName": "הקלע של יוני", "level": "19", "playerId": "8", "state": ""}, {"cityId": 326, "islandId": "1", "cityName": "שיש", "level": "68", "state": ""}, {"cityId": 513, "islandId": "1", "cityName": "Nico", "level": "17", "playerId": "247", "state": ""}])