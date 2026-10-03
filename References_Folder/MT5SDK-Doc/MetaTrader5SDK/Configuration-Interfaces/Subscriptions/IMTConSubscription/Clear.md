[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / Clear

[Previous](Assign.md) | [Next](ID.md)

# IMTConSubscription::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConSubscription::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
