package cities

import (
	"github.com/labstack/echo/v4"
)

func CitiesController(e *echo.Echo) {
	e.POST("/cities", postCities)
	e.GET("/cities", getCities)
}
