[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Tick Data](../Tick-Data.md) / TickHistoryRequest

[Previous](TickStat.md) | [Next](TickHistoryRequestRaw.md)

# IMTManagerAPI::TickHistoryRequest

Get quotes for a symbol in the specified time range.

C++
    
    
    MTAPIRES  IMTManagerAPI::TickHistoryRequest(
       LPCWSTR        symbol,          // Symbol
       const INT64    from,            // Start date
       const INT64    to,              // End date
       MTTickShort*&  ticks,           // Reference to the array of structures of quotes
       UINT&          ticks_total      // Number of quotes
       )

.NET
    
    
    MTTickShort[]  CIMTManagerAPI.TickHistoryRequest(
       string         symbol,          // Symbol
       long           from,            // Start date
       long           to,              // End date
       MTRetCode      res              // Response code
       )

Python
    
    
    ManagerAPI.TickHistoryRequest(
       symbol,        # Symbol
       from,          # Start date
       to             # End date
       )

### Parameters

**news**  
[in] The name of the symbol, for which you need to get quotes.

**from**  
[in] The start date for requesting quotes. The date is specified in seconds since January 1, 1970.

**to**  
[in] The end date for requesting quotes. The date is specified in seconds since January 1, 1970.

**ticks**  
[out] A reference to the array of structures that describe quotes (MTTickShort).

**ticks_total**  
[out] The total number of received quotes.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After being used, the array of structures [MTTickShort](../../../Structures/MTTickShort.md) must be released using the [IMTManagerAPI::Free](../Common-Functions/Free.md) method.
