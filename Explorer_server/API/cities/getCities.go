package cities

import (
	"context"
	"net/http"
	"time"

	"Explorer_server/DB/Collections"
	entities "Explorer_server/Entities"

	"github.com/labstack/echo/v4"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
)

func getCities(c echo.Context) error {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	citiesCollection := Collections.CitiesGetCollection()
	allyId := c.QueryParam("allyId")
	playerId := c.QueryParam("playerId")
	cityId := c.QueryParam("cityId")

	var filter bson.D
	if allyId != "" {
		//add later for ally
	} else if playerId != "" {
		filter = bson.D{primitive.E{Key: "player_id", Value: playerId}}
	} else if cityId != "" {
		filter = bson.D{primitive.E{Key: "city_id", Value: cityId}}
	} else {
		return c.String(http.StatusBadRequest, "bad query params")
	}

	var citiesList []entities.CityFull
	match := bson.D{primitive.E{Key: "$match", Value: filter}}
	lookUp := bson.D{primitive.E{Key: "$lookup", Value: bson.D{
		primitive.E{Key: "from", Value: "islands"},
		primitive.E{Key: "localField", Value: "island_id"},
		primitive.E{Key: "foreignField", Value: "island_id"},
		primitive.E{Key: "as", Value: "island"}}}}

	cursor, err := citiesCollection.Aggregate(ctx, mongo.Pipeline{match, lookUp})
	if err != nil {
		return c.String(http.StatusNotFound, err.Error())
	}
	if err = cursor.All(ctx, &citiesList); err != nil {
		return c.String(http.StatusInternalServerError, err.Error())
	}
	cities := entities.CitiesFullList{Cities: citiesList}

	return c.JSON(http.StatusOK, cities)
}
