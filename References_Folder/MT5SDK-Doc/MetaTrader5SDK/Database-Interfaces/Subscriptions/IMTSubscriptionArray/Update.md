[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTSubscriptionArray::Update

Change a subscription at the specified position of an array.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::Update(
       const UINT        pos,    // Position
       IMTSubscription*  record  // Subscription object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.Update(
       uint              pos,    // Position
       CIMTSubscription  record  // Subscription object
       )

### Parameters

**pos**  
[in] Position of a subscription in an array, starting at 0.

**record**  
[in]Subscription object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The IMTSubscriptionArray::Update method deletes the previous element ([IMTSubscription::Release](../IMTSubscription/Release.md) call) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (by the IMTSubscriptionArray::Release call), an earlier inserted object is automatically removed.

### Example
    
    
    //--- Example
       IMTSubscriptionArray *array=api->SubscriptionCreateArray();   
       IMTSubscription      *record1=api->SubscriptionCreate();
       IMTSubscription      *record2=api->SubscriptionCreate();
    //---
       array->Add(record1);
       array->Update(0,record2); // The first element (the 'record1' object) is replaced with record2
       //--- After that the 'record1' element will be released via Release, and the 'record2' lifetime will be controlled by the array
