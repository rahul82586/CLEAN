[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTClientArray::AddCopy

Add a copy of a client object at the end of an array.

C++
    
    
    MTAPIRES  IMTClientArray::AddCopy(
       const IMTClient*  client    // Client to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.AddCopy(
       CIMTClient        client    // Client to be added
       )

### Parameters

**client**  
[in]Client object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'client' object and places it at the end of the array.

# IMTOrderArray::AddCopy

Add copies of client objects into an array.

C++
    
    
    MTAPIRES  IMTClientArray::AddCopy(
       const IMTClientArray*  array      // Array of clients to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.AddCopy(
       CIMTClientArray        array      // Array of clients to be added
       )

### Parameters

**array**  
[in] An object of the clients array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the client objects belonging to the 'array' object, and inserts them at the end of the current array.
