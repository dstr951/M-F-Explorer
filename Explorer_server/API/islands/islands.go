package islands

import (
	"github.com/labstack/echo/v4"
)

func IslandsController(e *echo.Echo) {
	e.GET("/islands", getIslands)
	e.POST("/islands", postIsland)
}
