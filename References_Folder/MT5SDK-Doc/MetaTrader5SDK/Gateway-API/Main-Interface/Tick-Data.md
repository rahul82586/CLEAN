[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Main Interface](../Main-Interface.md) / Tick Data

[Previous](History-Data/ChartReplace.md) | [Next](Tick-Data/TickHistoryRequest.md)

# Tick Data Functions

The MetaTrader 5 Gateway API features functions for the export and import of tick data to the platform. Unlike [SendTicks*](Quote-and-News-Feeds/SendTicks.md), these functions work directly with the history of ticks, rather than the price stream which is broadcast to clients in real time.

Function | Purpose  
---|---  
[TickHistoryRequest](Tick-Data/TickHistoryRequest.md) | Get quotes for a symbol in the specified time range.  
[TickHistoryRequestRaw](Tick-Data/TickHistoryRequestRaw.md) | Get the entire stream of quotes for a symbol (raw and processed prices in accordance with the configuration of the symbol) in the specified time range.  
[TickHistoryAdd](Tick-Data/TickHistoryAdd.md) | Add tick data of a symbol.  
[TickHistoryReplace](Tick-Data/TickHistoryReplace.md) | Completely replace tick data in the specified period by the transmitted data
