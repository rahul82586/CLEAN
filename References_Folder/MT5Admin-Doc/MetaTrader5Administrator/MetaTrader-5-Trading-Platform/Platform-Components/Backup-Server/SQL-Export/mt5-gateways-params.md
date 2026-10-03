[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_gateways_params

[Previous](mt5-gateways.md) | [Next](mt5-gateways-translates.md)

# mt5_gateways_params

Data about [additional report settings (#parameters)](../../../Platform-Setup/Gateways/Configuration-of.md#parameters) is exported to this table. The table contains the following fields:

Name | Type | Description  
ParamID | String | The unique identifier of the parameter.  
GatewayName | String | The name of the gateway configuration the setting applies to.  
Type | Integer | Parameter type:

  * 0 — string
  * 1 — integer
  * 2 — floating-point number
  * 3 — time
  * 4 — date
  * 5 — date and time
  * 6 — list of groups
  * 7 — list of symbols

  
Name | String | Parameter name.  
Value | String | Parameter value.
