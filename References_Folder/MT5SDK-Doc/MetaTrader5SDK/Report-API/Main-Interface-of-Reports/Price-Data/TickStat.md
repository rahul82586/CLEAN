[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Price Data](../Price-Data.md) / TickStat

[Previous](TickLast.md) | [Next](TickHistoryGetRaw.md)

# IMTReportAPI::TickStat

Get statistical information about quotes for the specified symbol.
    
    
    MTAPIRES  IMTReportAPI::TickStat(
       LPCWSTR      symbol,     // Symbol
       MTTickStat&  stat        // Pointer to statistical data structure
       )

### Parameters

**symbol**  
[in] The symbol, for which you need to get information.

**stat**  
[out] A pointer to the structure that describes statistical price information (MTTickStat).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
