package entities

type CitiesFullList struct {
	Cities []CityFull `json:"cities" bson:"cities"`
}
