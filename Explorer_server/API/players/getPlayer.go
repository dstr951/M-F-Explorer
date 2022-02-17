package players

import (
	"context"
	"net/http"
	"time"

	"Explorer_server/DB/Collections"
	entities "Explorer_server/Entities"

	"github.com/labstack/echo/v4"
	"go.mongodb.org/mongo-driver/bson"
)

func getPlayer(c echo.Context) error {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	playersCollection := Collections.PlayersGetCollection()
	playerId := c.QueryParam("id")
	if playerId != "" {
		var player entities.Player
		if err := playersCollection.FindOne(ctx, bson.M{"player_id": playerId}).Decode(&player); err != nil {
			return c.String(http.StatusNotFound, err.Error())
		}
		return c.JSON(http.StatusOK, player)
	}
	playerName := c.QueryParam("name")
	var player entities.Player
	if err := playersCollection.FindOne(ctx, bson.M{"player_name": bson.M{"$regex": "^" + playerName + "$", "$options": "i"}}).Decode(&player); err != nil {
		return c.String(http.StatusNotFound, err.Error())
	}
	return c.JSON(http.StatusOK, player)

}
