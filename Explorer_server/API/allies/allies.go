package allies

import (
	"github.com/labstack/echo/v4"
)

func AlliesController(e *echo.Echo) {
	e.POST("/allies", postAllies)
	e.GET("/ally", getAlly)
}
