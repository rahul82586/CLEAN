[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Tick Data](../Tick-Data.md) / TickStat

[Previous](TickLast.md) | [Next](TickGet.md)

# IMTServerAPI::TickStat

Get statistical information about quotes for the specified symbol.
    
    
    MTAPIRES  IMTServerAPI::TickStat(
       LPCWSTR      symbol,     // Symbol
       MTTickStat&  stat        // A pointer to the structure of statistical information
       )

### Parameters

**symbol**  
[in] The symbol, for which you need to get information.

**stat**  
[out] A pointer to the structure that describes statistical price information (MTTickStat).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
