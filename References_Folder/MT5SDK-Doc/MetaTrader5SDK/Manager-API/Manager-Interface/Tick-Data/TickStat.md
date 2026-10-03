[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Tick Data](../Tick-Data.md) / TickStat

[Previous](TickLastRaw.md) | [Next](TickHistoryRequest.md)

# IMTManagerAPI::TickStat

Get statistical information about quotes for the specified symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::TickStat(
       LPCWSTR      symbol,     // Symbol
       MTTickStat&  stat        // Reference to the structure of statistical information
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TickStat(
       string          symbol,  // Symbol
       out MTTickStat  stat     // Statistical information structure
       )

Python
    
    
    ManagerAPI.TickStat(
       symbol          # Symbol
       )

### Parameters

**symbol**  
[in] The symbol, for which you need to get information.

**stat**  
[out] A reference to the structure that describes statistical price information (MTTickStat).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The symbol for which data are requested must be included into the [list of selected symbols](../Selected-Symbols.md).
