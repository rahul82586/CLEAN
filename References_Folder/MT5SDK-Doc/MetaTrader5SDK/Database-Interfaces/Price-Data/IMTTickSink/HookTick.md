[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Price Data](../../Price-Data.md) / [IMTTickSink](../IMTTickSink.md) / HookTick

[Previous](OnTickStat.md) | [Next](HookTickStat.md)

# IMTTickSink::HookTick

A hook of an event of new quote arrival.

C++
    
    
    virtual MTAPIRES  IMTTickSink::HookTick(
       const int   feeder,    // Data feed
       MTTick&     tick       // A reference to the structure of tick
       )

.NET (Manager API)
    
    
    virtual MTRetCode  CIMTTickSink.HookTick(
       int         feeder,    // Data feed
       ref MTTick  tick       // A reference to the structure of tick
       )

### Parameters

**feeder**  
[in] The data feed from which the quote is received.

**tick**  
[in][out] A reference to the structure of quote description (MTTick).

### Return Value

To accept a quote (to save it in the database), [MT_RET_OK](../../../Return-Codes/Successful-completion.md) should be returned. Any other response code should be returned to decline the quote.

### Note

This method is used only in the MetaTrader 5 Server API.
