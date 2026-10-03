[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionSymbol](../IMTConSubscriptionSymbol.md) / TickHistory

[Previous](Level.md) | [Next](../IMTConSubscriptionNews.md)

# IMTConAutomation::TickHistory

Get the depth of tick data available by subscription.

C++
    
    
    UINT64  IMTConAutomation::TickHistory()  const

.NET (Gateway/Manager API)
    
    
    EnFlags  CIMTConAutomation.TickHistory()

### Return Value

Depth of tick data as a value of the [IMTConSubscriptionSymbol::EnTickHistory (#entickhistory)](Enumerations.md#entickhistory) enumeration.

# IMTConAutomation::TickHistory

Set the depth of tick data available by subscription.

C++
    
    
    MTAPIRES  IMTConAutomation::TickHistory(
       const UINT64  mode   // Depth of tick data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.TickHistory(
       EnFlags       mode   // Depth of tick data
       )

### Parameters

**flags**  
[in]Depth of tick data as a value of theIMTConSubscriptionSymbol::EnTickHistoryenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
