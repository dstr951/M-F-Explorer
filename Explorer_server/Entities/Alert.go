package entities

import (
	"go.mongodb.org/mongo-driver/bson/primitive"
)

type Alert struct {
	AlertId     string              `json:"alertId" bson:"_id,omitempty"`
	AlertType   int                 `json:"alertType" bson:"alert_type"`
	AlertString string              `json:"alertString" bson:"alert_string"`
	TimeStamp   primitive.Timestamp `json:"timeStamp" bson:"time_stamp"`
	Item        string              `json:"item" bson:"item"`
	ItemId      string              `json:"itemId" bson:"item_id"`
}
