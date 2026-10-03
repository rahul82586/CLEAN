[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of End-of-Day Events](../Interface-of-End-of-Day-Events.md) / OnEODGroupStart

[Previous](OnEODStart.md) | [Next](OnEODGroupCommissions.md)

# IMTEndOfDaySink::OnEODGroupStart

A handler of the event of start of operations associated with the end of the trading day for the specified group.
    
    
    virtual void  IMTEndOfDaySink::OnEODGroupStart(
       const INT64         datetime,          // Time of the event
       const INT64         prev_datetime,     // Time of the previous event
       const IMTConGroup*  group              // Groups
       )

### Parameters

**datetime**  
[out] Time of the event in seconds that elapsed since 01.01.1970.

**prev_datetime**  
[out] Time of the previous similar event in seconds that elapsed since 01.01.1970.

**group**  
[out]The object of the group, with which the event is associated.
