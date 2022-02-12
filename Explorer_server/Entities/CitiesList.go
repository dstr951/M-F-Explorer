package entities

type CitiesList struct {
	Cities []City `json:"cities" bson:"cities"`
}
