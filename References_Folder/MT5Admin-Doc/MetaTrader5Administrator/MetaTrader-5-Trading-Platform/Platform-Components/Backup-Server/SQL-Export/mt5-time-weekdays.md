[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_time_weekdays

[Previous](mt5-time.md) | [Next](mt5-gateways.md)

# mt5_time_weekdays

Platform's [working time schedule (#daily-settings)](../../../Platform-Setup/Time.md#daily-settings) by days is exported to this table. The table contains the following fields:

Name | Type | Description  
TimeZone | Integer | The time zone of a server in minutes from GMT. For example: 0 = GMT, -60 = GMT - 1, 60 = GMT + 1. Corresponds to the TimeZone value in the [mt5_time](mt5-time.md) table.  
Day | Integer | The ordinal number of the day of the week. For example, 0 is Sunday, 6 is Saturday.  
00 | Integer | Flag of working time in the period from 00:00 to 00:59. 0 — non-working time, 1 — working time.  
01 | Integer | Flag of working time in the period from 01:00 to 01:59. 0 — non-working time, 1 — working time.  
... | Integer | Further similar fields apply for each hour of the day.  
23 | Integer | Flag of working time in the period from 23:00 to 23:59. 0 — non-working time, 1 — working time.
