[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTClientArray::Update

Change a client at the specified position of an array.

C++
    
    
    MTAPIRES  IMTClientArray::Update(
       const UINT  pos,       // Position
       IMTClient*  client     // Client object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.Update(
       uint        pos,       // Position
       CIMTClient  client     // Client object
       )

### Parameters

**pos**  
[in] Position of a client in an array, starting with 0.

**client**  
[in]Client object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The IMTClientArray::Update method deletes the previous element ([IMTClient::Release](../IMTClient/Release.md) call) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (by a call of IMTClientArray::Release), an earlier inserted object is automatically removed.

### Example
    
    
    //--- example
       IMTClientArray *array  =api->ClientCreateArray();   
       IMTClient      *client1=api->ClientCreate();
       IMTClient      *client2=api->ClientCreate();
    //---
       array->Add(client1);
       array->Update(0,client2); // the first element (object client1) is replaced by client2
       //--- after that the client1 element will be released via Release, and the client2 lifetime will be controlled by the array
