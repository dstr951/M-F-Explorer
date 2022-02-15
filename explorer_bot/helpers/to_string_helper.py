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
    buildingScore = "".join(playerJSON['buildingScore'].split(","))[:-2]
    researchScore = "".join(playerJSON['researchScore'].split(","))[:-2]
    armyScore = "".join(playerJSON['armyScore'].split(","))[:-2]
    allyString ="ללא ברית"
    if allyName != "":
        allyString = f"ברית: {allyName}"
    return f"סיכום לשחקן: {name} | מיקום בטבלה: {place} | {allyString}\n בנאים: {buildingScore} | גנרלים: {armyScore} | מחקרים: {researchScore}"

def city_to_string(cityJSON):
    name = cityJSON['cityName']
    level = cityJSON['level']
    state = cityJSON['state']    
    if state == "":
        state = "active"
    x = cityJSON['island'][0]['x']
    y = cityJSON['island'][0]['y']
    tradegood = cityJSON['island'][0]['tradegood']
    wonder = cityJSON['island'][0]['wonderName']
    wonder_level = cityJSON['island'][0]['wonderLevel']

    return f"{name} | [{x}:{y}]\nעיר רמה {level} | משאב: {resource_to_string(int(tradegood))} | פלא: {wonder} ברמה {wonder_level}\n"