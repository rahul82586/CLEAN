[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Main API Interface](../Main-API-Interface.md) / Tick Data

[Previous](History-Data/ChartSplit.md) | [Next](Tick-Data/TickSubscribe.md)

# Tick Data

The MetaTrader 5 Server API provides functions for working with tick data of the platform. They are used for adding quotes in the price stream, tracking incoming quotes and changing them if necessary.

Function | Purpose  
---|---  
[TickSubscribe](Tick-Data/TickSubscribe.md) | Subscribe to events and hooks associated with changes in the database of price data.  
[TickUnsubscribe](Tick-Data/TickUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the database of price data.  
[TickAdd](Tick-Data/TickAdd.md) | Add a quote into the price stream.  
[TickAddBatch](Tick-Data/TickAddBatch.md) | Add multiple quotes into the price stream.  
[TickAddStat](Tick-Data/TickAddStat.md) | Add statistical information about the price.  
[TickLast](Tick-Data/TickLast.md) | Get the las quote for the specified symbol.  
[TickStat](Tick-Data/TickStat.md) | Get statistical information about quotes for the specified symbol.  
[TickGet](Tick-Data/TickGet.md) | Get quotes for a symbol in the specified time range.  
[TickHistoryGetRaw](Tick-Data/TickHistoryGetRaw.md) | Get the entire stream of quotes for a symbol (raw and processed prices in accordance with the configuration of the symbol) in the specified time range.  
[TickHistoryGet](Tick-Data/TickHistoryGet.md) | Get the history of quotes processed in accordance with the symbol configuration in the specified time range.
