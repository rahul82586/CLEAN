[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Tick Data](../Tick-Data.md) / TickHistoryRequestRaw

[Previous](TickHistoryRequest.md) | [Next](TickHistoryAdd.md)

# IMTGatewayAPI::TickHistoryRequestRaw

Get the entire stream of quotes for a symbol (raw and processed prices in accordance with the configuration of the symbol) in the specified time range.

C++
    
    
    MTAPIRES  IMTGatewayAPI::TickHistoryRequestRaw(
       LPCWSTR        symbol,          // Symbol
       const INT64    from,            // Beginning date
       const INT64    to,              // End date
       MTTickRate*&   ticks,           // Link to an array of quote structures
       UINT&          ticks_total      // Number of quotes
       )

.NET
    
    
    MTTickRate[]  CIMTGatewayAPI.TickHistoryRequestRaw(
       string         symbol,          // Symbol
       long           from,            // Beginning date
       long           to,              // End date
       out MTRetCode  res              // Response code
       )

### Parameters

**symbol**  
[in] The name of the symbol, for which you need to get quotes.

**from**  
[in] The start date for requesting quotes. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end date for requesting quotes. The date is specified in seconds since 01.01.1970.

**ticks**  
[out] A reference to the array of structures which describe quotes (MTTickRate).

**ticks_total**  
[out] The total number of received quotes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

If the raw quote storing option ([IMTConSymbol::TickFlags](../../../Configuration-Interfaces/Symbols/IMTConSymbol/TickFlags.md)) is disabled in symbol settings, only the quote which were accepted by the server are received, i.e. the operation is similar to the [IMTAdminAPI::TickRequest](../../../Manager-API/Administrator-Interface/Tick-Data/TickRequest.md) method call.

After the use, the [MTTickRate](../../../Structures/MTTickRate.md) array of structures must be released using the [IMTGatewayAPI::Free](../Common-Functions/Free.md) method.

The method cannot be called from event handlers (any IMT*Sink class methods).
