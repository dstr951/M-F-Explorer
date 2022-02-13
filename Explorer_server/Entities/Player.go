package entities

type Player struct {
	PlayerId             string `json:"playerId" bson:"player_id"`
	PlayerName           string `json:"playerName" bson:"player_name"`
	AllyId               string `json:"allyId" bson:"ally_id"`
	Place                string `json:"place" bson:"place"`
	State                string `json:"state" bson:"state"`
	BuildingScore        string `json:"buildingScore" bson:"building_score"`
	ResearchScore        string `json:"researchScore" bson:"research_score"`
	ArmyScore            string `json:"armyScore" bson:"army_score"`
	TraderSecondaryScore string `json:"traderSecondaryScore" bson:"trader_secondary_score"`
}
