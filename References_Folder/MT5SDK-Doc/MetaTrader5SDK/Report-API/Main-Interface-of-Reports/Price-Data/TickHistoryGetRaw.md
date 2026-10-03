[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Price Data](../Price-Data.md) / TickHistoryGetRaw

[Previous](TickStat.md) | [Next](TickHistoryGet.md)

# IMTReportAPI::TickHistoryGetRaw

Get raw quotes (not processed prices in accordance with the configuration of the symbol) for a symbol in the specified time range.
    
    
    MTAPIRES  IMTReportAPI::TickHistoryGetRaw(
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

Reports work on trade server, and the history data is requested from the databases of the history server. Note, that each call of the method leads to a network request to the history server. Frequent calls of the method may decrease the performance. 
