package citiesScripts

import (
	"context"
	"reflect"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"

	"Explorer_server/DB/Collections"
	entities "Explorer_server/Entities"
)

func AddCities(ctx context.Context, cities entities.CitiesList) error {
	citiesCollection := Collections.CitiesGetCollection()
	for _, city := range cities.Cities {
		var c entities.City
		if err := citiesCollection.FindOne(ctx, bson.M{"city_id": city.CityId}).Decode(&c); err != nil {
			if err == mongo.ErrNoDocuments {
				_, err := citiesCollection.InsertOne(ctx, city)
				if err != nil {
					return err
				}
			} else {
				return err
			}
		}
		if equal := reflect.DeepEqual(c, city); !equal {
			//here we will update alerts later
			_, err := citiesCollection.ReplaceOne(ctx, bson.M{"city_id": city.CityId}, city)
			if err != nil {
				return err
			}
		}
	}

	return nil
}
