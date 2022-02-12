package cities

import (
	"context"
	"net/http"
	"time"

	citiesScripts "Explorer_server/DB/Scripts/cities"
	entities "Explorer_server/Entities"

	"github.com/labstack/echo/v4"
)

func postCities(c echo.Context) (err error) {
	cit := new(entities.CitiesList)
	if err = c.Bind(cit); err != nil {
		return err
	}

	cities := entities.CitiesList{
		Cities: cit.Cities,
	}

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	if err = citiesScripts.AddCities(ctx, cities); err != nil {
		return c.String(http.StatusInternalServerError, err.Error())
	}

	return c.NoContent(http.StatusCreated)
}
