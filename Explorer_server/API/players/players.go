package players

import (
	"github.com/labstack/echo/v4"
)

func PlayersController(e *echo.Echo) {
	e.POST("/players", postPlayers)
	e.GET("/players", getPlayers)
	e.GET("/player", getPlayer)
}
