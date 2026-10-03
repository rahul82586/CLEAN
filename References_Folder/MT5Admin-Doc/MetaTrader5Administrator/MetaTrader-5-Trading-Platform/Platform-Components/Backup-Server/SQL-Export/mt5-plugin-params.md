[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_plugin_params

[Previous](mt5-plugins.md) | [Next](mt5-time.md)

# mt5_plugin_params

Data about [additional plugin settings (#module)](../../../Platform-Setup/Plugins.md#module) is exported to this table. The table contains the following fields:

Name | Type | Description  
ParamID | String | The unique identifier of the parameter.  
Plugin | String | The name of the plugin, to which the setting applies.  
Server | Integer | The ID of the trade server, for which the plugin is configured.  
Type | Integer | Parameter type:

  * 0 — string
  * 1 — integer
  * 2 — floating-point number
  * 3 — time
  * 4 — date
  * 5 — date and time
  * 6 — list of groups
  * 7 — list of symbols

  
Name | String | The name of the parameter.  
Value | String | The value of the parameter.
