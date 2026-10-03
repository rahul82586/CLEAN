[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Price Data](../../Price-Data.md) / [IMTTickSink](../IMTTickSink.md) / HookTickStat

[Previous](HookTick.md) | [Next](../IMTChartSink.md)

# IMTTickSink::HookTickStat

A hook of an event of update of the statistical information about a price.

C++
    
    
    virtual MTAPIRES  IMTTickSink::HookTickStat(
       const int       feeder,  // Data feed
       MTTickStat&     stat     // A reference to the statistics description structure
       )

.NET (Manager API)
    
    
    virtual MTAPIRES  CIMTTickSink.HookTickStat(
       int             feeder,  // Data feed
       ref MTTickStat  stat     // A reference to the statistics description structure
       )

### Parameters

**feeder**  
[in] The data feed from which the quote is received.

**stat**  
[in][out] A reference to the structure that describes statistical price information (MTTickStat).

### Return Value

To accept the data (to save it in the database), [MT_RET_OK](../../../Return-Codes/Successful-completion.md) should be returned. Any other response code should be returned to decline the data.

### Note

This method is used only in the MetaTrader 5 Server API.
