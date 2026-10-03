[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistoryArray](../IMTSubscriptionHistoryArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTSubscriptionHistoryArray::UpdateCopy

Change a subscription action at the specified position of an array by copying the parameters of a passed action object.

C++
    
    
    MTAPIRES  IMTSubscriptionHistoryArray::UpdateCopy(
       const UINT                     pos,    // Position
       const IMTSubscriptionHistory*  record  // Action object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistoryArray.UpdateCopy(
       uint                           pos,    // Position
       CIMTSubscriptionHistory        record  // Action object
       )

### Parameters

**pos**  
[in] Position of a subscription action in an array, starting at 0.

**record**  
[in]Subscription action object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This method copies the 'record' object parameters to the subscription object at the specified position in the array.
