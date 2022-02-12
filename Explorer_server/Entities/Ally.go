package entities

type Ally struct {
	AllyId   string `json:"allyId" bson:"ally_id"`
	AllyName string `json:"allyName" bson:"ally_name"`
}
