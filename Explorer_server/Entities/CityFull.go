package entities

type CityFull struct {
	CityId   int      `json:"cityId" bson:"city_id"`
	IslandId string   `json:"islandId" bson:"island_id"`
	CityName string   `json:"cityName" bson:"city_name"`
	Level    string   `json:"level" bson:"level"`
	PlayerId string   `json:"playerId" bson:"player_id"`
	State    string   `json:"state" bson:"state"`
	Island   []Island `json:"island" bson:"island"`
}
