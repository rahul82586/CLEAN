[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Tick Data](../Tick-Data.md) / TickRequest

[Previous](../Tick-Data.md) | [Next](TickRequestRaw.md)

# IMTAdminAPI::TickRequest

Get quotes for a symbol in the specified time range.

C++
    
    
    MTAPIRES  IMTAdminAPI::TickRequest(
       LPCWSTR        symbol,          // Symbol
       const INT64    from,            // Start date
       const INT64    to,              // End date
       MTTickShort*&  ticks,           // Reference to the array of structures of quotes
       UINT&          ticks_total      // Number of quotes
       )

.NET
    
    
    MTTickShort[]  CIMTAdminAPI.TickRequest(
       string         symbol,          // Symbol
       long           from,            // Start date
       long           to,              // End date
       out MTRetCode  res              // Response code
       )

Python
    
    
    AdminAPI.TickRequest(
       symbol,        # Symbol
       from,          # Start date
       to             # End date
       )

### Parameters

**symbol**  
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

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After being used, the array of structures [MTTickShort](../../../Structures/MTTickShort.md) must be released using the [IMTAdminAPI::Free](../Common-Functions/Free.md) method.
