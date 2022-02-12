import requests

def postIsland(island_json):
    url = "http://localhost:9000/islands"       
    res = requests.post(url, json= island_json)  
    return res   

#leave for testing
#postIsland({"islandId": "1", "type": 4, "name": "Mirruos", "x": 50, "y": 50,"tradegood": "2", "tradegoodTarget": "noluxury", "resourceLevel": "15", "tradegoodLevel": "11", "wonder": "1", "wonderLevel": "14", "wonderName": "הנפחייה של הפסטוס", "cityId_0": 30, "cityId_1": 6015, "cityId_2": 1967, "cityId_3": 1963, "cityId_4": 38, "cityId_5": 34, "cityId_6": 2648, "cityId_7": 936, "cityId_8": 5847, "cityId_9": 407, "cityId_10": 39, "cityId_11": 90, "cityId_12": 1290, "cityId_13": 5057, "cityId_14": 646, "cityId_15": 326, "cityId_16": 513})
