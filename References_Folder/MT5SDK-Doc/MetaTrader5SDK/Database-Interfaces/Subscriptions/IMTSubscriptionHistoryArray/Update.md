[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistoryArray](../IMTSubscriptionHistoryArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTSubscriptionHistoryArray::Update

Change a subscription action at the specified position of an array.

C++
    
    
    MTAPIRES  IMTSubscriptionHistoryArray::Update(
       const UINT               pos,    // Position
       IMTSubscriptionHistory*  record  // Action object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistoryArray.Update(
       uint                     pos,    // Position
       CIMTSubscriptionHistory  record  // Action object
       )

### Parameters

**pos**  
[in] Position of a subscription action in an array, starting at 0.

**record**  
[in]Subscription action object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The IMTSubscriptionHistoryArray::Update method deletes the previously existing element (by calling [IMTSubscriptionHistory::Release](../IMTSubscriptionHistory/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (by <IMTSubscriptionHistoryArray::Release call), an earlier inserted object will be automatically deleted.

### Example
    
    
    //--- Example
       IMTSubscriptionHistoryArray *array=api->SubscriptionHistoryCreateArray();   
       IMTSubscriptionHistory      *record1=api->SubscriptionHistoryCreate();
       IMTSubscriptionHistory      *record2=api->SubscriptionHistoryCreate();
    //---
       array->Add(record1);
       array->Update(0,record2); // The first element (the 'record1' object) is replaced with record2
       //--- After that the 'record1' element will be released via Release, and the 'record2' lifetime will be controlled by the array
