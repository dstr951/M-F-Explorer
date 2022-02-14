package allies

import (
	"context"
	"net/http"
	"time"

	"Explorer_server/DB/Collections"
	entities "Explorer_server/Entities"

	"github.com/labstack/echo/v4"
	"go.mongodb.org/mongo-driver/bson"
)

func getAlly(c echo.Context) error {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	AlliesCollection := Collections.AlliesGetCollection()
	allyId := c.QueryParam("id")
	if allyId != "" {
		var ally entities.Ally
		if err := AlliesCollection.FindOne(ctx, bson.M{"ally_id": allyId}).Decode(&ally); err != nil {
			return c.String(http.StatusNotFound, err.Error())
		}
		return c.JSON(http.StatusOK, ally)
	}
	allyName := c.QueryParam("name")
	var ally entities.Ally
	if err := AlliesCollection.FindOne(ctx, bson.M{"ally_name": allyName}).Decode(&ally); err != nil {
		return c.String(http.StatusNotFound, err.Error())
	}
	return c.JSON(http.StatusOK, ally)

}
