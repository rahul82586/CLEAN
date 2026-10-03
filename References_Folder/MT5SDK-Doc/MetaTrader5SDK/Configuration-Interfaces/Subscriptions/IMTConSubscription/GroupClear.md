[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / GroupClear

[Previous](GroupDelete.md) | [Next](GroupShift.md)

# IMTConSubscription::GroupClear

Clear the list of groups for which the subscription is available.

C++
    
    
    MTAPIRES  IMTConSubscription::GroupClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.GroupClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This method deletes all groups from the list.
