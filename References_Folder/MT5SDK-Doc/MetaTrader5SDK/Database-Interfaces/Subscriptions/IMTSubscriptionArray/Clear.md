[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTSubscriptionArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
