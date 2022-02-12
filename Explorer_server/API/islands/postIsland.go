package islands

import (
	"context"
	"net/http"
	"time"

	islandsScripts "Explorer_server/DB/Scripts/islands"
	entities "Explorer_server/Entities"

	"github.com/labstack/echo/v4"
)

func postIsland(c echo.Context) (err error) {
	i := new(entities.Island)
	if err = c.Bind(i); err != nil {
		return err
	}

	island := entities.Island{
		IslandId:        i.IslandId,
		Type:            i.Type,
		Name:            i.Name,
		X:               i.X,
		Y:               i.Y,
		Tradegood:       i.Tradegood,
		TradegoodTarget: i.TradegoodTarget,
		TesourceLevel:   i.TesourceLevel,
		TradegoodLevel:  i.TradegoodLevel,
		Wonder:          i.Wonder,
		WonderLevel:     i.WonderLevel,
		WonderName:      i.WonderName,
		CityId_0:        i.CityId_0,
		CityId_1:        i.CityId_1,
		CityId_2:        i.CityId_2,
		CityId_3:        i.CityId_3,
		CityId_4:        i.CityId_4,
		CityId_5:        i.CityId_5,
		CityId_6:        i.CityId_6,
		CityId_7:        i.CityId_7,
		CityId_8:        i.CityId_8,
		CityId_9:        i.CityId_9,
		CityId_10:       i.CityId_10,
		CityId_11:       i.CityId_11,
		CityId_12:       i.CityId_12,
		CityId_13:       i.CityId_13,
		CityId_14:       i.CityId_14,
		CityId_15:       i.CityId_15,
		CityId_16:       i.CityId_16,
	}

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	if err = islandsScripts.AddIsland(ctx, island); err != nil {
		return c.String(http.StatusInternalServerError, err.Error())
	}

	return c.NoContent(http.StatusCreated)
}
