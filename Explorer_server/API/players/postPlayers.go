package players

import (
	"context"
	"net/http"
	"time"

	playersScripts "Explorer_server/DB/Scripts/players"
	entities "Explorer_server/Entities"

	"github.com/labstack/echo/v4"
)

func postPlayers(c echo.Context) (err error) {
	p := new(entities.PlayersList)
	if err = c.Bind(p); err != nil {
		return err
	}

	players := entities.PlayersList{
		Players: p.Players,
	}

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	if err = playersScripts.AddPlayers(ctx, players); err != nil {
		return c.String(http.StatusInternalServerError, err.Error())
	}

	return c.NoContent(http.StatusCreated)
}
