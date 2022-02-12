package entities

type PlayersList struct {
	Players []Player `json:"players" bson:"players"`
}
