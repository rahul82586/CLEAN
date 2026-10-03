[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_holidays

[Previous](mt5-daily-positions.md) | [Next](mt5-network.md)

# mt5_holidays

Data about [holidays](../../../Platform-Setup/Holidays.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Year | Integer | The year of a holiday. 0 stands for yearly holidays.  
Month | Integer | Month of a holiday (1 — January, 12 — December).  
Day | Integer | Day of a holiday.  
From | Integer | Holiday start time. Specified in a number of minutes from 00:00. For example, 600 corresponds to 10:00.  
To | Integer | Holiday end time. Specified in a number of minutes from 00:00. For example, 1200 corresponds to 20:00.  
Description | String | Holiday description (no more than 128 symbols).  
Timestamp | Integer | A unique value within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has been changed.  
Mode | Integer | Holiday mode. 0 — holiday disabled, 1 — enabled.  
Symbols | String | The list of financial instruments or their groups, for which a holiday is valid. Instruments and groups are separated by comma, for example: "EURUSD,CFD\*".
