[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of End-of-Day Events](../Interface-of-End-of-Day-Events.md) / OnEOMGroupFinish

[Previous](OnEOMGroupStatements.md) | [Next](OnEOMFinish.md)

# IMTEndOfDaySink::OnEOMGroupFinish

A handler of the event of completion of operations associated with the end of the trading month for the specified group.
    
    
    virtual void  IMTEndOfDaySink::OnEOMGroupFinish(
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
