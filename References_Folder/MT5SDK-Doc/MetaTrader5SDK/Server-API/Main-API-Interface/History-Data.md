[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Main API Interface](../Main-API-Interface.md) / History Data

[Previous](Trade/Request-Processing/DealerRequestGetAll.md) | [Next](History-Data/ChartSubscribe.md)

# History Data

The MetaTrader 5 Server API provides functions for working with historical price data of the platform that are available in the form of minute bars. They allow you to edit or delete minute bars.

Functions for working with historical data:

Function | Purpose  
---|---  
[ChartSubscribe](History-Data/ChartSubscribe.md) | Subscribe to events and hooks associated with changes in the database of one-minute data.  
[ChartUnsubscribe](History-Data/ChartUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the database of one-minute data.  
[ChartGet](History-Data/ChartGet.md) | Request minute bars for a symbol.  
[ChartDelete](History-Data/ChartDelete.md) | Delete a bar by the symbol.  
[ChartUpdate](History-Data/ChartUpdate.md) | Change historical data of a symbol.  
[ChartSplit](History-Data/ChartSplit.md) | Split of the symbol's bar history.  
  
> Price data is stored on the history server in the form of one minute bars. Larger timeframes are formed on a client side from the minute bars according to the following principle: bars from the first to the last second of a period are used for calculation. For example, a H1 bar for 13:00 consists of minute bars within the range from 13:00:00 to 13:59:59.
