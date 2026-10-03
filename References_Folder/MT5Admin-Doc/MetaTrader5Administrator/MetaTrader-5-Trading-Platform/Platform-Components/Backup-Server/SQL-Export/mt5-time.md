[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_time

[Previous](mt5-plugin-params.md) | [Next](mt5-time-weekdays.md)

# mt5_time

Platform [trading time settings](../../../Platform-Setup/Time.md) are exported to this table. The table contains the following fields:

Name | Type | Description  
TimeZone | Integer | The time zone of a server in minutes from GMT. For example: 0 = GMT, -60 = GMT - 1, 60 = GMT + 1.  
Timestamp | Integer | A unique value within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has changed.  
TimeServer | String | The address of the current time synchronization server.  
Daylight | Integer | Daylight Saving Time mode: 0 — off, 1 — on.  
DaylightState | Integer | The presence of the daylight saving time in the platform time zone. 0 means no daylight saving time is applied in the platform time zone. Otherwise, any non-zero value is used.
