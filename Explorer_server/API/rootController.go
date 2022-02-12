package rootController

import (
	allies "Explorer_server/API/allies"
	cities "Explorer_server/API/cities"
	islands "Explorer_server/API/islands"
	players "Explorer_server/API/players"

	"github.com/labstack/echo/v4"
)

func RootController(e *echo.Echo) {
	islands.IslandsController(e)
	players.PlayersController(e)
	cities.CitiesController(e)
	allies.AlliesController(e)
}
