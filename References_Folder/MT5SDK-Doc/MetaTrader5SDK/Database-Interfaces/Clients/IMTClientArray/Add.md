[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTClientArray::Add

Add a client object at the end of an array.

C++
    
    
    MTAPIRES  IMTClientArray::Add(
       IMTClient*  client    // Client to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.Add(
       CIMTClient  client    // Client to be added
       )

### Parameters

**client**  
[in]Client object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the lifetime of the 'client' object is passed to the array object. Thus, when deleting an array object (by a call of [IMTClientArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTClientArray::Add

Add a client array object at the end of an array.

C++
    
    
    MTAPIRES  IMTClientArray::Add(
       IMTClientArray*  array      // Array of clients to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.Add(
       CIMTClientArray  array      // Array of clients to be added
       )

### Parameters

**array**  
[in] An object of the clients array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the 'array' object, at the end of the current array and clears the 'array' object.

### Example
    
    
    //--- example
       IMTClientArray *array =api->ClientCreateArray();   
       IMTClient      *client=api->ClientCreate();
    //---
       array->Add(client);  // after that the lifetime is controlled by the array
       array->Delete(0);    // delete the first element, after that a pointer in 'client' becomes invalid ('Release' was called)
     
    //--- Incorrect use example
       IMTClientArray  *array =api->ClientCreateArray();   
       IMTClient       *client=api->ClientCreate();
    //---
       array->Add(client);
       array->Add(client); // in this case the array will contain two pointers to one and the same object!
       //--- an attempt to clear the array will lead to crash, because this will be an attempt to delete the object twice
