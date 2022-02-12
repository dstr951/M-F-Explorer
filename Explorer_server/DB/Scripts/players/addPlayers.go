package playersScripts

import (
	"context"
	"reflect"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"

	"Explorer_server/DB/Collections"
	entities "Explorer_server/Entities"
)

func AddPlayers(ctx context.Context, players entities.PlayersList) error {
	playersCollection := Collections.PlayersGetCollection()
	for _, player := range players.Players {
		var p entities.Player
		if err := playersCollection.FindOne(ctx, bson.M{"player_id": player.PlayerId}).Decode(&p); err != nil {
			if err == mongo.ErrNoDocuments {
				_, err := playersCollection.InsertOne(ctx, player)
				if err != nil {
					return err
				}
			} else {
				return err
			}
		}
		if equal := reflect.DeepEqual(p, player); !equal {
			//here we will update alerts later
			_, err := playersCollection.ReplaceOne(ctx, bson.M{"player_id": player.PlayerId}, player)
			if err != nil {
				return err
			}
		}
	}

	return nil
}
