[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_feeder_translates

[Previous](mt5-feeders/Enumerations.md) | [Next](mt5-feeder-params.md)

# mt5_feeder_translates

Data about [conversion settings of data feeds (#translation)](../../../Platform-Setup/Data-Feeds/Configuration-of.md#translation) is exported to this table. The table contains the following fields:

Name | Type | Description  
Symbol | String | The name of the symbol in the trading platform.  
Feeder | String | The name of the data feed, to which the conversion setting applies.  
Source | String | The name of the symbol on the source server.  
BidMarkup | Integer | Markup for the symbol's Bid price received from the data feed.  
AskMarkup | Integer | Markup for the symbol's Ask price received from the data feed.  
Digits | Integer | The number of digits after the decimal point in the price of the symbol that receives quotes.
