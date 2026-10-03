[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of End-of-Day Events](../Interface-of-End-of-Day-Events.md) / OnEODGroupRollovers

[Previous](OnEODGroupStatements.md) | [Next](OnEODGroupFinish.md)

# IMTEndOfDaySink::OnEODGroupRollovers

A handler of the event of start of rollover charging for the specified group at the end of the trading day.
    
    
    virtual void  IMTEndOfDaySink::OnEODGroupRollovers(
       const INT64         datetime,          // Time of the event
       const INT64         prev_datetime,     // Time of the previous event
       const IMTConGroup*  group              // Group
       )

### Parameters

**datetime**  
[out] Time of the event in seconds that elapsed since 01.01.1970.

**prev_datetime**  
[out] Time of the previous similar event in seconds that elapsed since 01.01.1970.

**group**  
[out]The object of the group, with which the event is associated.
