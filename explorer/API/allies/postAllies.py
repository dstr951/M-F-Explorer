import requests

def postAllies(allies_json):
    url = "http://localhost:9000/allies"  
    data = {"allies": allies_json}  
    res = requests.post(url, json= data)  
    return res  

#leave for testing
#postAllies([{"allyId": "1", "allyName": "BoS"}, {"allyId": "6", "allyName": "REIGN"}, {"allyId": "40", "allyName": "LDV"}, {"allyId": "19", "allyName": "-NR-"}])