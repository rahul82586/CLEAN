[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTOnlineArray::Add

Add connection record object at the end of an array.

C++
    
    
    MTAPIRES  IMTOnlineArray::Add(
       IMTOnline*  online      // Added connection record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.Add(
       CIMTOnline  online      // Added connection record
       )

### Parameters

**online**  
[in] Connection record object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the user object is passed to the array object. Thus, when deleting an array object (call of [IMTOnlineArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTOnlineArray::Add

Add connection record array object at the end of an array.

C++
    
    
    MTAPIRES  IMTOnlineArray::Add(
       IMTOnlineArray*  array      // Added connection record array
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.Add(
       CIMTOnlineArray  array      // Added connection record array
       )

### Parameters

**array**  
[in] Connection record array object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

### Example
    
    
    //--- Example
       IMTOnlineArray *array=api->OnlineCreateArray();   
       IMTOnline      *online=api->OnlineCreate();
    //---
       array->Add(online);  // After that the lifetime is controlled by the array
       array->Delete(0);    // Deleting the first element, then the pointer in 'user' becomes invalid (Release was called)
     
    //--- Example of incorrect use
       IMTOnlineArray *array=api->OnlineCreateArray();   
       IMTOnline      *online=api->OnlineCreate();
    //---
       array->Add(online);
       array->Add(online); // In this case the array will have two pointers to one and the same object!
       //--- Array clearing will cause crash, because two attempts will be made to delete the same object
