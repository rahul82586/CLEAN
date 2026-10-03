[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistory](../IMTSubscriptionHistory.md) / Action

[Previous](Record.md) | [Next](Time.md)

# IMTSubscriptionHistory::Action

Get the type of performed subscription action.

C++
    
    
    UINT  IMTSubscriptionHistory::Action()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTSubscriptionHistory.Action()

### Return Value

Action type as a value of the [IMTSubscriptioHistory::EnAction (#enaction)](Enumerations.md#enaction) enumeration.

# IMTSubscriptionHistory::Action

Set the type of action performed with the subscription.

C++
    
    
    MTAPIRES  IMTSubscriptionHistory::Action(
       const UINT  status     // Action type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistory.Action(
       uint        status     // Action type
       )

### Parameters

**status**  
[in] Action type as a value of theIMTSubscriptioHistory::EnActionenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
