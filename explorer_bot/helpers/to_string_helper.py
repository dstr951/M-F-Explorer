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

def player_to_string(playerJSON, allyJSON):
    name = playerJSON['playerName']
    allyName = allyJSON['allyName']
    place = playerJSON['place']
    buildingScore = "".join(playerJSON['buildingScore'].split(","))[:-2]
    researchScore = "".join(playerJSON['researchScore'].split(","))[:-2]
    armyScore = "".join(playerJSON['armyScore'].split(","))[:-2]
    return f"סיכום לשחקן: {name} מיקום בטבלה: {place} ברית: {allyName}\n בנאים: {buildingScore}, גנרלים: {armyScore} מחקרים: {researchScore}"

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

    return f"{name} [{x}:{y}]\nעיר רמה {level}, סוג משאב {resource_to_string(int(tradegood))}\n פלא: {wonder} ברמה {wonder_level}\n"