[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_feeder_params

[Previous](mt5-feeder-translates.md) | [Next](mt5-feeder-symbols.md)

# mt5_feeder_params

Data about [additional settings of data feeds (#parameters)](../../../Platform-Setup/Data-Feeds/Configuration-of.md#parameters) is exported to this table. The table contains the following fields:

Name | Type | Description  
ParamID | String | The unique identifier of the parameter.  
Feeder | String | The name of the data feed, to which the setting applies.  
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
