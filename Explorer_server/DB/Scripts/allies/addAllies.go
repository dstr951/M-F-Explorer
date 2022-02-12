package alliesScripts

import (
	"context"
	"reflect"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"

	"Explorer_server/DB/Collections"
	entities "Explorer_server/Entities"
)

func AddAlly(ctx context.Context, allies entities.AlliesList) error {
	alliesCollection := Collections.AlliesGetCollection()
	for _, ally := range allies.Allies {
		var a entities.City
		if err := alliesCollection.FindOne(ctx, bson.M{"ally_id": ally.AllyId}).Decode(&a); err != nil {
			if err == mongo.ErrNoDocuments {
				_, err := alliesCollection.InsertOne(ctx, ally)
				if err != nil {
					return err
				}
			} else {
				return err
			}
		}
		if equal := reflect.DeepEqual(a, ally); !equal {
			//here we will update alerts later
			_, err := alliesCollection.ReplaceOne(ctx, bson.M{"ally_id": ally.AllyId}, ally)
			if err != nil {
				return err
			}
		}
	}

	return nil
}
