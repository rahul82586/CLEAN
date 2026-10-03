[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of End-of-Day Events](../Interface-of-End-of-Day-Events.md) / OnEODFinish

[Previous](OnEODGroupFinish.md) | [Next](OnEOMStart.md)

# IMTEndOfDaySink::OnEODFinish

A handler of the event of completion of operations associated with the end of the trading day.
    
    
    virtual void  IMTEndOfDaySink::OnEODFinish(
       const INT64  datetime,          // Time of the event
       const INT64  prev_datetime      // Time of the previous event
       )

### Parameters

**datetime**  
[out] Time of the event in seconds that elapsed since 01.01.1970.

**prev_datetime**  
[out] Time of the previous similar event in seconds that elapsed since 01.01.1970.
