package islands

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func getIslands(c echo.Context) error {
	return c.JSON(http.StatusOK, nil)
}
