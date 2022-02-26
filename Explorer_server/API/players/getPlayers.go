package players

import (
	"context"
	"fmt"
	"net/http"
	"time"

	"Explorer_server/DB/Collections"
	entities "Explorer_server/Entities"

	"github.com/labstack/echo/v4"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
)

func getPlayers(c echo.Context) error {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	playersCollection := Collections.PlayersGetCollection()
	allyId := c.QueryParam("allyId")
	allyName := c.QueryParam("allyName")

	var filter bson.D
	if allyId != "" {
		filter = bson.D{primitive.E{Key: "ally_id", Value: allyId}}
	} else if allyName != "" {
		AlliesCollection := Collections.AlliesGetCollection()
		var ally entities.Ally
		if err := AlliesCollection.FindOne(ctx, bson.M{"ally_name": allyName}).Decode(&ally); err != nil {
			return c.String(http.StatusNotFound, fmt.Sprintf("ally with the name %s wasn't found", allyName))
		}
		filter = bson.D{primitive.E{Key: "ally_id", Value: ally.AllyId}}
	} else {
		return c.String(http.StatusBadRequest, "bad query params")
	}

	var playersList []entities.Player

	cursor, err := playersCollection.Find(ctx, filter)
	if err != nil {
		return c.String(http.StatusInternalServerError, err.Error())
	}
	if err = cursor.All(ctx, &playersList); err != nil {
		return c.String(http.StatusInternalServerError, err.Error())
	}
	if playersList == nil {
		var ally_error_string string
		if allyId != "" {
			ally_error_string = fmt.Sprintf("id %s", allyId)
		} else if allyName != "" {
			ally_error_string = fmt.Sprintf("name %s", allyName)
		}
		return c.String(http.StatusNotFound, fmt.Sprintf("ally with the %s doesn't have any players", ally_error_string))
	}
	players := entities.PlayersList{Players: playersList}

	return c.JSON(http.StatusOK, players)
}
