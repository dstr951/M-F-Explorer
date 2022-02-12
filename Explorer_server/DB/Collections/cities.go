package Collections

import (
	"Explorer_server/DB"

	"go.mongodb.org/mongo-driver/mongo"
)

func CitiesGetCollection() *mongo.Collection {
	return DB.Client.Database("Explorer").Collection("cities")
}
