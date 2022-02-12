package allies

import (
	"context"
	"net/http"
	"time"

	alliesScripts "Explorer_server/DB/Scripts/allies"
	entities "Explorer_server/Entities"

	"github.com/labstack/echo/v4"
)

func postAllies(c echo.Context) (err error) {
	a := new(entities.AlliesList)
	if err = c.Bind(a); err != nil {
		return err
	}

	allies := entities.AlliesList{
		Allies: a.Allies,
	}

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	if err = alliesScripts.AddAlly(ctx, allies); err != nil {
		return c.String(http.StatusInternalServerError, err.Error())
	}

	return c.NoContent(http.StatusCreated)
}
