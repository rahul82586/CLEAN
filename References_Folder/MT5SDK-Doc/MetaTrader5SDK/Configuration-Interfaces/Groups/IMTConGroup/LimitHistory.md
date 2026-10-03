[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / LimitHistory

[Previous](DemoInactivityPeriod.md) | [Next](LimitOrders.md)

# IMTConGroup::LimitHistory

Get the maximum number of days, for which the group can request data on conducted trade operation.

C++
    
    
    UINT  IMTConGroup::LimitHistory()  const

.NET (Gateway/Manager API)
    
    
    EnHistoryLimit  CIMTConGroup.LimitHistory()

Python (Manager API)
    
    
    MTConGroup.LimitHistory

### Return Value

A value from [IMTConGroup::EnHistoryLimit (#enhistorylimit)](Enumerations.md#enhistorylimit).

# IMTConGroup::LimitHistory

Set the maximum number of days, for which the group can request data on conducted trade operation.

C++
    
    
    MTAPIRES  IMTConGroup::LimitHistory(
       const UINT      limit  // A limit of the trading history
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.LimitHistory(
       EnHistoryLimit  limit  // A limit of the trading history
       )

Python (Manager API)
    
    
    MTConGroup.LimitHistory

### Parameters

**limit**  
[in] TheIMTConGroup::EnHistoryLimitenumeration is used for passing the limit of the trading operations history.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
