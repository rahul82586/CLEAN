[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistoryArray](../IMTSubscriptionHistoryArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTSubscriptionHistoryArray::Add

Add a subscription action object to the end of an array.

C++
    
    
    MTAPIRES  IMTSubscriptionHistoryArray::Add(
       IMTSubscriptionHistory*  record  // Action to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistoryArray.Add(
       CIMTSubscriptionHistory  record  // Action to be added
       )

### Parameters

**record**  
[in]Subscription action object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the lifetime of the 'record' object is passed to the array object. Thus, when deleting an array object (by [IMTSubscriptionHistoryArray::Release](Release.md) call), an earlier inserted object will be automatically deleted.

# IMTSubscriptionHistoryArray::Add

Add an object of an array of subscription actions to the end of an array.

C++
    
    
    MTAPIRES  IMTSubscriptionHistoryArray::Add(
       IMTSubscriptionHistoryArray*  array   // Array of actions to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.Add(
       CIMTSubscriptionHistoryArray  array   // Array of actions to be added
       )

### Parameters

**array**  
[in] Object of an array of actions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers contained in the 'array' object, at the end of the current array and clears the 'array' object.

### Example
    
    
    //--- Example
       IMTSubscriptionHistoryArray *array=api->SubscriptionHistoryCreateArray();   
       IMTSubscriptionHistory      *record=api->SubscriptionHistoryCreate();
    //---
       array->Add(record); // After that the lifetime is controlled by the array
       array->Delete(0);   // Delete the first element, after that a pointer in 'record' becomes invalid ('Release' was called)
     
    //--- Incorrect use example
       IMTSubscriptionHistoryArray *array=api->SubscriptionHistoryCreateArray();   
       IMTSubscriptionHistory      *record=api->SubscriptionHistoryCreate();
    //---
       array->Add(record);
       array->Add(record); // In this case the array will contain two pointers to one and the same object!
       //--- An attempt to clear the array will lead to crash, because this will be an attempt to delete the object twice
