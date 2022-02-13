package Collections

import (
	"Explorer_server/DB"

	"go.mongodb.org/mongo-driver/mongo"
)

func AlertsGetCollection() *mongo.Collection {
	return DB.Client.Database("Explorer").Collection("alerts")
}
