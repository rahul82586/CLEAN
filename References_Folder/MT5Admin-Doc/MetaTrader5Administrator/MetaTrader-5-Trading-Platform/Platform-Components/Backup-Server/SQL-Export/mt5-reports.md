[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_reports

[Previous](mt5-feeder-symbols.md) | [Next](mt5-report-params.md)

# mt5_reports

Data about [report settings](../../../Platform-Setup/Reports.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Name | String | The name of the report configuration.  
Server | Integer | The ID of the trade server, for which the report is configured.  
Timestamp | Integer | A unique value within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has been changed.  
Module | String | The name of the report module.  
Mode | Integer | Report operation mode: 0 — disabled, 1 — enabled.
