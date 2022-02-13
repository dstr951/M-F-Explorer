package alertsScripts

import (
	"context"

	"Explorer_server/DB/Collections"
	entities "Explorer_server/Entities"
)

func AddAlert(ctx context.Context, alert entities.Alert) error {
	alertsCollection := Collections.AlertsGetCollection()
	_, err := alertsCollection.InsertOne(ctx, alert)
	if err != nil {
		return err
	}
	return nil
}
