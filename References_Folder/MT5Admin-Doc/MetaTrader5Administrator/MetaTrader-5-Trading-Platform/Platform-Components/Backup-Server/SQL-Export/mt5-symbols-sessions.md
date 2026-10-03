[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_symbols_sessions

[Previous](mt5-symbols/Enumerations.md) | [Next](mt5-groups.md)

# mt5_symbols_sessions

Data on symbols' trade and quoting sessions is exported to the table. The table contains the following fields:

Name | Type | Description  
Session_ID | Integer | Primary key. Unique session ID. Assigned automatically during the export.  
Symbol_ID | Integer | Unique [ID of the symbol](mt5-symbols.md), to which the session is applied.  
Type | Integer | Session type: 0 - quoting, 1 - trade.  
Day | Integer | Day of the week from 0 to 6. 0 - Sunday, 6 - Saturday.  
Open | Integer | The opening time of a trading or quoting session of a symbol in minutes elapsed since 00:00. For example, 100 denotes 01:40.  
Close | Integer | The closing time of a trading or quoting session of a symbol in minutes elapsed since 00:00.
