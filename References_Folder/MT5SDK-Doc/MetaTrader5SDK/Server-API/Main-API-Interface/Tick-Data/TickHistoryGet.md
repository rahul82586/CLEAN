[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Tick Data](../Tick-Data.md) / TickHistoryGet

[Previous](TickHistoryGetRaw.md) | [Next](../Depth-of-Market.md)

# IMTServerAPI::TickHistoryGet

Get the history of quotes processed in accordance with the symbol configuration in the specified time range.
    
    
    MTAPIRES  IMTServerAPI::TickHistoryGet(
       LPCWSTR              symbol,          // Symbol
       const INT64          from,            // Start date
       const INT64          to,              // End date
       MTTickShort*&        ticks,           // A pointer to the array of structures of quotes
       UINT&                ticks_total      // Number of quotes
       )

### Parameters

**symbol**  
[in] The name of the symbol, for which you need to get quotes.

**from**  
[in] The start date for requesting quotes. The date is specified in seconds since January 1, 1970.

**to**  
[in] The end date for requesting quotes. The date is specified in seconds since January 1, 1970.

**ticks**  
[out] A pointer to the array of structures that describe quotes (MTTickShort).

**ticks_total**  
[out] The total number of received quotes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method can be used on both history and trade servers.
