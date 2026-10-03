[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTSubscriptionArray::Add

Add a subscription object to the end of an array.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::Add(
       IMTSubscription*  record  // Subscription to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.Add(
       CIMTSubscription  record  // Subscription to be added
       )

### Parameters

**record**  
[in]Subscription object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the lifetime of the 'record' object is passed to the array object. Thus, when deleting an array object (by [IMTSubscriptionArray::Release](Release.md) call), an earlier inserted object is automatically removed.

# IMTSubscriptionArray::Add

Add a subscription object to the end of an array.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::Add(
       IMTSubscriptionArray*  array   // Array of subscriptions to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.Add(
       CIMTSubscriptionArray  array   // Array of subscriptions to be added
       )

### Parameters

**array**  
[in] An object of the array of subscriptions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers contained in the 'array' object, at the end of the current array and clears the 'array' object.

### Example
    
    
    //--- Example
       IMTSubscriptionArray *array=api->SubscriptionCreateArray();   
       IMTSubscription      *record=api->SubscriptionCreate();
    //---
       array->Add(record); // After that the lifetime is controlled by the array
       array->Delete(0);   // Delete the first element, after that a pointer in 'record' becomes invalid ('Release' was called)
     
    //--- Incorrect use example
       IMTSubscriptionArray *array=api->SubscriptionCreateArray();   
       IMTSubscription      *record=api->SubscriptionCreate();
    //---
       array->Add(record);
       array->Add(record); // In this case the array will contain two pointers to one and the same object!
       //--- An attempt to clear the array will lead to crash, because this will be an attempt to delete the object twice
