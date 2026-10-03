[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_plugins

[Previous](mt5-report-params.md) | [Next](mt5-plugin-params.md)

# mt5_plugins

Data about [plugin settings](../../../Platform-Setup/Plugins.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Name | String | The name of the plugin configuration.  
Server | Integer | The ID of the trade server, for which the plugin is configured.  
Timestamp | Integer | A unique value within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has been changed.  
Module | String | The name of the plugin module.  
Enable | Integer | Plugin operation mode: 0 — disabled, 1 — enabled.  
Flags | Integer | Plugin operation flags:

  * 0 — no flags
  * 1 — permission to configure the plugin from a manager terminal
  * 2 — the profiling mode enabled


