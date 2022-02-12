package islandsScripts

import (
	"context"
	"reflect"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"

	"Explorer_server/DB/Collections"
	entities "Explorer_server/Entities"
)

func AddIsland(ctx context.Context, island entities.Island) error {
	islandsCollection := Collections.IslandsGetCollection()
	var i entities.Island
	if err := islandsCollection.FindOne(ctx, bson.M{"island_id": island.IslandId}).Decode(&i); err != nil {
		if err == mongo.ErrNoDocuments {
			_, err := islandsCollection.InsertOne(ctx, island)
			if err != nil {
				return err
			}
		} else {
			return err
		}
	}
	if equal := reflect.DeepEqual(i, island); !equal {
		//here we will update alerts later
		_, err := islandsCollection.ReplaceOne(ctx, bson.M{"island_id": island.IslandId}, island)
		if err != nil {
			return err
		}
	}

	return nil
}
