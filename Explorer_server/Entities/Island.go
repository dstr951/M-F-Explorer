package entities

type Island struct {
	IslandId        string `json:"islandId" bson:"island_id"`
	Type            int    `json:"type" bson:"type"`
	Name            string `json:"name" bson:"name"`
	X               int    `json:"x" bson:"x"`
	Y               int    `json:"y" bson:"y"`
	Tradegood       string `json:"tradegood" bson:"tradegood"`
	TradegoodTarget string `json:"tradegoodTarget" bson:"tradegood_target"`
	TesourceLevel   string `json:"resourceLevel" bson:"resource_level"`
	TradegoodLevel  string `json:"tradegoodLevel" bson:"tradegood_level"`
	Wonder          string `json:"wonder" bson:"wonder"`
	WonderLevel     string `json:"wonderLevel" bson:"wonderLevel"`
	WonderName      string `json:"wonderName" bson:"wonderName"`
	CityId_0        int    `json:"cityId_0" bson:"city_id_0"`
	CityId_1        int    `json:"cityId_1" bson:"city_id_1"`
	CityId_2        int    `json:"cityId_2" bson:"city_id_2"`
	CityId_3        int    `json:"cityId_3" bson:"city_id_3"`
	CityId_4        int    `json:"cityId_4" bson:"city_id_4"`
	CityId_5        int    `json:"cityId_5" bson:"city_id_5"`
	CityId_6        int    `json:"cityId_6" bson:"city_id_6"`
	CityId_7        int    `json:"cityId_7" bson:"city_id_7"`
	CityId_8        int    `json:"cityId_8" bson:"city_id_8"`
	CityId_9        int    `json:"cityId_9" bson:"city_id_9"`
	CityId_10       int    `json:"cityId_10" bson:"city_id_10"`
	CityId_11       int    `json:"cityId_11" bson:"city_id_11"`
	CityId_12       int    `json:"cityId_12" bson:"city_id_12"`
	CityId_13       int    `json:"cityId_13" bson:"city_id_13"`
	CityId_14       int    `json:"cityId_14" bson:"city_id_14"`
	CityId_15       int    `json:"cityId_15" bson:"city_id_15"`
	CityId_16       int    `json:"cityId_16" bson:"city_id_16"`
}
