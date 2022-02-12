import re
import json

def __init__():
    pass

def getIsland(html):
    """This function uses the html passed to it as a string to extract, parse and return an Island object
    
    Parameters
    ----------
    html : str
        the html returned when a get request to view the island is made. This request can be made with the following statement: ``s.get(urlIsla + islandId)``, where ``urlIsla`` is a string defined in ``config.py`` and ``islandId`` is the id of the island.

    Returns
    -------
    island : Island
        this function returns a json parsed Island object. For more information about this object refer to the github wiki page of Ikabot.
    """
    isla = re.search(r'\[\["updateBackgroundData",([\s\S]*?),"specialServerBadges', html).group(1) + '}'

    isla = isla.replace('buildplace', 'empty')
    isla = isla.replace('xCoord', 'x')
    isla = isla.replace('yCoord', 'y')
    isla = isla.replace(',"owner', ',"')

    # {"id":idIsla,"name":nombreIsla,"x":,"y":,"good":numeroBien,"woodLv":,"goodLv":,"wonder":numeroWonder, "wonderName": "nombreDelMilagro","wonderLv":"5","cities":[{"type":"city","name":cityName,"id":cityId,"level":lvIntendencia,"Id":playerId,"Name":playerName,"AllyId":,"AllyTag":,"state":"vacation"},...}}
    isla = json.loads(isla, strict=False)
    isla['tipo'] = re.search(r'"tradegood":"(\d)"', html).group(1)
    isla['x'] = int(isla['x'])
    isla['y'] = int(isla['y'])

    return isla

def re_island(island_raw):
    """This function uses the Ikabot_Island object passed to it to create an Explorer_Island object for explorer DB
    Parameters
    ----------
    island_raw : Ikabot_Island
        the object that's returned from the getIsland function.

    Returns
    -------
    island_json : Explorer_Island
        this function returns a json parsed Explorer_Island.
    """
    island_id = island_raw["id"]
    island_type = island_raw["type"]
    name= island_raw["name"]
    x= island_raw["x"]
    y= island_raw["y"]
    tradegood= island_raw["tradegood"]
    tradegoodTarget = island_raw["tradegoodTarget"]
    resourceLevel = island_raw["resourceLevel"]
    tradegoodLevel = island_raw["tradegoodLevel"]
    wonder = island_raw["wonder"]
    wonderLevel = island_raw["wonderLevel"] 
    wonderName = island_raw["wonderName"]    
    cities = island_raw["cities"]
    city_ids=[]
    for city in cities:
        if city["type"] == "empty":
            city_ids.append(None)
        else:
            city_ids.append(city["id"])    
    island_json = {
        "islandId":island_id,
        "type":island_type,
        "name": name,
        "x": x,
        "y": y,
        "tradegood": tradegood,
        "tradegoodTarget": tradegoodTarget,
        "resourceLevel": resourceLevel,
        "tradegoodLevel": tradegoodLevel,
        "wonder": wonder,
        "wonderLevel": wonderLevel,
        "wonderName": wonderName,
        "cityId_0": city_ids[0],
        "cityId_1": city_ids[1],
        "cityId_2": city_ids[2],
        "cityId_3": city_ids[3],
        "cityId_4": city_ids[4],
        "cityId_5": city_ids[5],
        "cityId_6": city_ids[6],
        "cityId_7": city_ids[7],
        "cityId_8": city_ids[8],
        "cityId_9": city_ids[9],
        "cityId_10": city_ids[10],
        "cityId_11": city_ids[11],
        "cityId_12": city_ids[12],
        "cityId_13": city_ids[13],
        "cityId_14": city_ids[14],
        "cityId_15": city_ids[15],
        "cityId_16": city_ids[16],       
    }
    return island_json

def re_cities_players_allies(island_raw):
    """This function uses the Ikabot_Island object passed to it to create an Explorer_Island object for explorer DB
    
    Parameters
    ----------
    island_raw : Ikabot_Island
        the object that's returned from the getIsland function.

    Returns
    -------
    cities_json : Explorer_Cities, palyers_json : Explorer_Players, allies_json : Explorer_Allies
        
    """
    cities = island_raw["cities"]
    cities_json = []
    players_json = []
    allies_json = []
    for city in cities:
        if city["type"] != "city":
            continue
        island_id = island_raw["id"]
        cityName = city["name"]
        cityId = city["id"]
        level = city["level"]
        playerId = city["Id"]  
        state = city["state"]
        city_json={
            "cityId": cityId,
            "islandId": island_id,
            "cityName": cityName,            
            "level": level,
            "playerId": playerId,            
            "state": state,
        }        
        cities_json.append(city_json)


        avatars = island_raw["avatarScores"]
        playerName = city["Name"]
        allyId = city["AllyId"] 
        if playerId in avatars:
            place = avatars[playerId]["place"]
            buildingScore = avatars[playerId]["building_score_main"]
            researchScore = avatars[playerId]["research_score_main"]
            armyScore = avatars[playerId]["army_score_main"]
            traderSecondaryScore = avatars[playerId]["trader_score_secondary"]
        else:
            place = ""
            buildingScore = ""
            researchScore = ""
            armyScore = ""
            traderSecondaryScore = ""
        player_json = {
            "playerId": playerId,
            "playerName": playerName,
            "allyId": allyId,
            "place": place,
            "buildingScore": buildingScore,
            "researchScore": researchScore,
            "armyScore": armyScore,
            "traderSecondaryScore": traderSecondaryScore,
        }
        player_exists = next((x for x in players_json if x["playerId"] == playerId), None)
        if not player_exists:
            players_json.append(player_json)        
        if allyId != "0":            
            allyName = city["AllyTag"]
            ally_json = {
                "allyId": allyId,
                "allyName": allyName,
            }
            ally_exists = next((x for x in allies_json if x["allyId"] == allyId), None)
            if not ally_exists:
                allies_json.append(ally_json)
            

    return cities_json, players_json, allies_json


def reassembleIsland(island_html):
    """This function uses the html passed to it as a string to extract, parse and return 4 Explorer object ready for the DB
    Parameters
    ----------
    island_html : str
        the html returned when a get request to view the island is made. This request can be made with the following statement: ``s.get(urlIsla + islandId)``, where ``urlIsla`` is a string defined in ``config.py`` and ``islandId`` is the id of the island.

    Returns
    -------
    island_json : Explorer_Island, cities_json : Explorer_Cities, palyers_json : Explorer_Players, allies_json : Explorer_Allies
    """
    island_raw = getIsland(island_html)
    island_json = re_island(island_raw)
    cities_json, players_json, allies_json = re_cities_players_allies(island_raw)
    return island_json, cities_json, players_json, allies_json
