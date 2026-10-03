[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Manager Interface](../Manager-Interface.md) / Tick Data

[Previous](History-Data/ChartSplit.md) | [Next](Tick-Data/TickSubscribe.md)

# Tick Data Functions

The MetaTrader 5 Manager API provides functions for working with tick prices of the platform. They are used for adding quotes in the price stream and tracking incoming quotes.

Functions for working with price data:

Function | Purpose  
---|---  
[TickSubscribe](Tick-Data/TickSubscribe.md) | Subscribe to the events associated with changes in the database of price data.  
[TickUnsubscribe](Tick-Data/TickUnsubscribe.md) | Unsubscribe from the events associated with changes in the database of price data.  
[TickAdd](Tick-Data/TickAdd.md) | Add a quote into the price stream.  
[TickAddBatch](Tick-Data/TickAddBatch.md) | Add multiple quotes into the price stream.  
[TickAddStat](Tick-Data/TickAddStat.md) | Add statistical information about the price.  
[TickLast](Tick-Data/TickLast.md) | Get the last quote of a symbol taking into account spread difference settings for the current manager's group or another specified group.  
[TickLastRaw](Tick-Data/TickLastRaw.md) | Get the last raw quote of a symbol.  
[TickStat](Tick-Data/TickStat.md) | Get statistical information about quotes for the specified symbol.  
[TickHistoryRequest](Tick-Data/TickHistoryRequest.md) | Get quotes for a symbol in the specified time range.  
[TickHistoryRequestRaw](Tick-Data/TickHistoryRequestRaw.md) | Get the entire stream of quotes for a symbol (raw and processed prices in accordance with the configuration of the symbol) in the specified time range.  
[TickHistoryAdd](Tick-Data/TickHistoryAdd.md) | Add tick data for a symbol.  
[TickHistoryReplace](Tick-Data/TickHistoryReplace.md) | Full replacement of tick data in the specified period with the passed data.
