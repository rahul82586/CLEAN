[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_prices

[Previous](mt5-accounts.md) | [Next](mt5-daily.md)

# mt5_prices

Price data of financial instruments is exported to the table. The table contains the following fields:

Name | Type | Description  
Price_ID | Integer | Primary key. Unique symbol ID for more efficient request of the data from the database. Assigned automatically during the export.  
Symbol | String | Symbol name.  
Digits | Integer | The number of decimal places in the price.  
Time | DateTime | The time of quotes coming in the format YYYY-MM-DD HH:MM:SS.  
BidLast | Float | The Bid price.  
BidLow | Float | The lowest bid price for the current day .  
BidHigh | Float | The highest bid price for the current day.  
BidDir | Integer | The direction of change of the bid price relative to its previous state (0 — unchanged, 1 — upwards, 2 — downwards).  
AskLast | Float | The Ask price.  
AskLow | Float | The lowest ask price for the current day.  
AskHigh | Float | The highest ask price for the current day.  
AskDir | Integer | The direction of change of the ask price relative to its previous state (0 — unchanged, 1 — upwards, 2 — downwards).  
LastLast | Float | The price of the last committed transaction.  
LastLow | Float | The lowest price, at which a deal was executed during the current day.  
LastHigh | Float | The highest price, at which a deal was executed during the current day.  
LastDir | Integer | The change direction of the price of the last deal relative to its previous state (0 — unchanged, 1 — upwards, 2 — downwards).
