[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Administrator Interface](../Administrator-Interface.md) / Tick Data

[Previous](History-Data/ChartSplit.md) | [Next](Tick-Data/TickRequest.md)

# Tick Data Functions

The MetaTrader 5 Manager API provides functions for working with tick data of the platform. They are used for adding quotes in the price stream, tracking incoming quotes and changing them if necessary.

Functions for working with price data:

Function | Purpose  
---|---  
[TickRequest](Tick-Data/TickRequest.md) | Get quotes for a symbol in the specified time range.  
[TickRequestRaw](Tick-Data/TickRequestRaw.md) | Get the entire stream of quotes for a symbol (raw and processed prices in accordance with the configuration of the symbol) in the specified time range.  
[TickAdd](Tick-Data/TickAdd.md) | Add tick data for a symbol.  
[TickReplace](Tick-Data/TickReplace.md) | Full replacement of tick data in the specified period with the passed data.
