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

def player_to_string(playerJSON):
    name = playerJSON['playerName']
    #add ally
    place = playerJSON['place']
    return f"סיכום לשחקן, {name} מיקום: {place}"

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

    return f"שם העיר: {name}, [{x},{y}] רמה {level}, סוג משאב {resource_to_string(int(tradegood))}, פלא: {wonder} ברמה {wonder_level}"