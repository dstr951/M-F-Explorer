package playersScripts

import (
	"context"
	"reflect"
	"strings"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"

	"Explorer_server/DB/Collections"
	alertsScripts "Explorer_server/DB/Scripts/alerts"
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
			if p.State != player.State {
				alertType := 0
				var alertString string
				if p.State == "" || p.State == "noob" {
					if strings.Contains(player.State, "banned") {
						alertType = 11
						alertString = "שחקן קיבל באן"
					} else if player.State == "vacation" {
						alertType = 12
						alertString = "שחקן יצא לחופשה"
					} else if player.State == "inactive" {
						alertType = 13
						alertString = "שחקן הפך ללא פעיל"
					}
				} else if p.State == "vacation" {
					if player.State == "" {
						alertType = 16
						alertString = "שחקן חזר מחופשה"
					}
				} else if p.State == "inactive" {
					if player.State == "" {
						alertType = 15
						alertString = "שחקן חזר להיות פעיל"
					}
				} else if p.State == "noob" {
					if player.State == "" {
						alertType = 14
						alertString = "שחקן ירד מהגנת אלים"
					}
				}
				if alertType != 0 {
					newAlert := entities.Alert{
						AlertType:   alertType,
						AlertString: alertString,
						TimeStamp:   primitive.Timestamp{T: uint32(time.Now().Unix())},
						Item:        "playerId",
						ItemId:      p.PlayerId,
					}
					alertsScripts.AddAlert(ctx, newAlert)
				}
			}
			_, err := playersCollection.ReplaceOne(ctx, bson.M{"player_id": player.PlayerId}, player)
			if err != nil {
				return err
			}
		}
	}

	return nil
}
