[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistoryArray](../IMTSubscriptionHistoryArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTSubscriptionHistoryArray::Delete

Delete a subscription action object by position.

C++
    
    
    MTAPIRES  IMTSubscriptionHistoryArray::Delete(
       const UINT  pos      // Action position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistoryArray.Delete(
       uint        pos      // Action position
       )

### Parameters

**pos**  
[in] Position of a subscription action in an array, starting at 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The deleted object will be automatically released by [IMTSubscriptionHistory::Release](../IMTSubscriptionHistory/Release.md) call.
