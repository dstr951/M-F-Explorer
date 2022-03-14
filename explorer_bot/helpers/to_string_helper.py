def resource_to_string(resource_id):
    if resource_id == 1:
        return "יין"
    if resource_id == 2:
        return "שיש"
    if resource_id == 3:
        return "קריסטל"
    if resource_id == 4:
        return "גופרית"
    return "שגיאה בהמרת המשאב"

def player_to_string(playerJSON, allyName):
    name = playerJSON['playerName']    
    place = playerJSON['place']
    statusHEB = convert_status_to_HEB(playerJSON['state'])
    
    buildingScore = "".join(playerJSON['buildingScore'].split(","))[:-2]
    researchScore = "".join(playerJSON['researchScore'].split(","))[:-2]
    armyScore = "".join(playerJSON['armyScore'].split(","))[:-2]
    allyString ="ללא ברית"
    if allyName != "":
        allyString = f"ברית: {allyName}"
    return f"שחקן: {name} | מיקום בטבלה: {place} | סטאטוס: {statusHEB} | {allyString}\n בנאים: {buildingScore} | גנרלים: {armyScore} | מחקרים: {researchScore}"

def city_to_string(cityJSON, minimal):
    name = cityJSON['cityName']
    level = cityJSON['level']    
    x = cityJSON['island'][0]['x']
    y = cityJSON['island'][0]['y']
    tradegood = cityJSON['island'][0]['tradegood']
    wonder = cityJSON['island'][0]['wonderName']
    wonder_level = cityJSON['island'][0]['wonderLevel']
    if minimal:
        return f"{name} | [{x}:{y}]\n"
    return f"{name} | [{x}:{y}]\nעיר רמה {level} | משאב: {resource_to_string(int(tradegood))} | פלא: {wonder} ברמה {wonder_level}\n"

def convert_status_to_HEB(statusENG):
    if statusENG.find("banned") != -1:
        return "באן"
    return {
        "":"פעיל",
        "inactive":"לא פעיל",
        "vacation":"בחופשה",
        "noob":"הגנת אלים"        
    }.get(statusENG, "שגיאה בסטאטוס")