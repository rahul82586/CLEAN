[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistoryArray](../IMTSubscriptionHistoryArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTSubscriptionHistoryArray::AddCopy

Add a copy of a subscription action object to the end of an array.

C++
    
    
    MTAPIRES  IMTSubscriptionHistoryArray::AddCopy(
       const IMTSubscriptionHistory*  record   // Action to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistoryArray.AddCopy(
       CIMTSubscription               record   // Action to be added
       )

### Parameters

**record**  
[in]Subscription action object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'record' object and places it at the end of the array.

# IMTSubscriptionHistoryArray::AddCopy

Add copies of subscription action objects to an array.

C++
    
    
    MTAPIRES  IMTSubscriptionHistoryArray::AddCopy(
       const IMTSubscriptionHistoryArray*  array   // Array of actions to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistoryArray.AddCopy(
       CIMTSubscriptionHistoryArray        array   // Array of actions to be added
       )

### Parameters

**array**  
[in] Object of an array of subscription actions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of order objects belonging to the 'array' object, and inserts them at the end of the current array.
