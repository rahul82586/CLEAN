[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTSubscriptionArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::Assign(
       const IMTSubscriptionArray*  array    // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatchingArray.Assign(
       CIMTSubscriptionArray        array    // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
