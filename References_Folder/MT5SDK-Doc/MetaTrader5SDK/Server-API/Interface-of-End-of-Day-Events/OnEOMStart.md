[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of End-of-Day Events](../Interface-of-End-of-Day-Events.md) / OnEOMStart

[Previous](OnEODFinish.md) | [Next](OnEOMGroupStart.md)

# IMTEndOfDaySink::OnEOMStart

A handler of the event of start of operations associated with the end of the trading month.
    
    
    virtual void  IMTEndOfDaySink::OnEOMStart(
       const INT64  datetime,          // Time of the event
       const INT64  prev_datetime      // Time of the previous event
       )

### Parameters

**datetime**  
[out] Time of the event in seconds that elapsed since 01.01.1970.

**prev_datetime**  
[out] Time of the previous similar event in seconds that elapsed since 01.01.1970.

### Note

The time of the end of the trading month is set using the [IMTConServerTrade::OvernightTime](../../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md) method (end of the last trading day).
