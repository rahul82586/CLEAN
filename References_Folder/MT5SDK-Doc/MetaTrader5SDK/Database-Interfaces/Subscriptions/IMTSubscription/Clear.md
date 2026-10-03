[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / Clear

[Previous](Assign.md) | [Next](ID.md)

# IMTSubscription::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTSubscription::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscription.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
