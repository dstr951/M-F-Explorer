package main

import (
	"log"
	"os"

	"github.com/joho/godotenv"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"

	rootController "Explorer_server/API"
	"Explorer_server/DB"
)

func main() {
	DB.InitClient()

	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	e := echo.New()

	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// change with dotenv later to remove origins
	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins:     []string{"http://localhost:5000"},
		AllowCredentials: true,
	}))

	rootController.RootController(e)

	e.Logger.Fatal(e.Start(":" + os.Getenv("PORT")))
}
