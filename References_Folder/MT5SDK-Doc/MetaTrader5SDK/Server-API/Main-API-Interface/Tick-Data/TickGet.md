[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Tick Data](../Tick-Data.md) / TickGet

[Previous](TickStat.md) | [Next](TickHistoryGetRaw.md)

# IMTServerAPI::TickGet

Get accepted quotes for a symbol in the specified time range.
    
    
    MTAPIRES  IMTServerAPI::TickGet(
       LPCWSTR        symbol,          // Symbol
       const INT64    from,            // Start date
       const INT64    to,              // End date
       MTTickShort*&  ticks,           // A pointer to the array of structures of quotes
       UINT&          ticks_total      // Number of quotes
       )

### Parameters

**symbol**  
[in] The name of the symbol, for which you need to get quotes.

**from**  
[in] The start date for requesting quotes. The date is specified in seconds since January 1, 1970. If the parameter is set to 0, the date of the first available quote is used.

**to**  
[in] The end date for requesting quotes. The date is specified in seconds since January 1, 1970. If the parameter is set to 0, the date of the last available quote is used.

**ticks**  
[out] A pointer to the array of structures that describe quotes (MTTickShort).

**ticks_total**  
[out] The total number of received quotes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method returns only accepted quotes (but not processed in accordance with the symbol settings of the group).

# IMTServerAPI::TickGet

Get quotes processed in accordance with the symbol configuration in the specified time range.
    
    
    MTAPIRES  IMTServerAPI::TickGet(
       const IMTConSymbol*  symbol,          // Symbol configuration object
       const INT64          from,            // Start date
       const INT64          to,              // End date
       MTTickShort*&        ticks,           // A pointer to the array of structures of quotes
       UINT&                ticks_total      // Number of quotes
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration. The symbol object must be first created using theIMTServerAPI::SymbolCreatemethod.

**from**  
[in] The start date for requesting quotes. The date is specified in seconds since January 1, 1970. If the parameter is set to 0, the date of the first available quote is used.

**to**  
[in] The end date for requesting quotes. The date is specified in seconds since January 1, 1970. If the parameter is set to 0, the date of the last available quote is used.

**ticks**  
[out] A pointer to the array of structures that describe quotes (MTTickShort).

**ticks_total**  
[out] The total number of received quotes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

When using the method on a trade server, it returns a buffer with last accepted quotes (up to 128 last quotes for each symbol).
