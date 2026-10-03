[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTOnlineArray::Update

Change a connection record at the specified position of an array.

C++
    
    
    MTAPIRES  IMTOnlineArray::Update(
       const UINT  pos,       // Position
       IMTUser*    user       // Connection record object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.Update(
       uint        pos,       // Position
       CIMTUser    user       // Connection record object
       )

### Parameters

**pos**  
[in] Position of a connection record in an array, starting with 0.

**online**  
[in] Connection record object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTOnlineArray::Update method deletes the previous element (call of [IMTOnline::Release](../IMTOnline/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of IMTOnlineArray::Release), an earlier inserted object is automatically removed.

### Example
    
    
    //--- Example
       IMTOnlineArray  *array =api->OnlineCreateArray();   
       IMTOnline       *online1=api->OnlineCreate();
       IMTOnline       *online2=api->OnlineCreate();
    //---
       array->Add(online1);
       array->Update(0,online2); // The first element (object online1) is replace by online2
       //--- After that the online1 element will be released through Release, and the lifetime of online2 will be controlled by the array
