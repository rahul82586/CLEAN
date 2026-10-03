[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_gateways_translates

[Previous](mt5-gateways-params.md) | [Next](mt5-gateways-symbols.md)

# mt5_gateways_translates

Data about [price translation settings in the gateway (#translation)](../../../Platform-Setup/Gateways/Configuration-of.md#translation) is exported to this table. The table contains the following fields:

Name | Type | Description  
Symbol | String | The name of the symbol in the trading platform.  
GatewayName | String | The name of the gateway configuration the setting applies to.  
Server | Integer | The ID of the trade server, for which the plugin is configured.  
Source | String | The symbol name in the data feed, to which the gateway connects.  
BidMarkup | Integer | Correction for the Bid price received for a symbol from the data source, to which the gateway connects.  
AskMarkup | Integer | Correction for the Ask price received for a symbol from the data source, to which the gateway connects.  
Digits | Integer | The number of digits after the decimal point in the price of the symbol that receives quotes.
