[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTOnlineArray::AddCopy

Add a copy of connection record object at the end of an array.

C++
    
    
    MTAPIRES  IMTOnlineArray::AddCopy(
       const IMTOnline*  online      // Added connection record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.AddCopy(
       CIMTOnline        online      // Added connection record
       )

### Parameters

**online**  
[in] Connection record object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the user object and places it at the end of the array.

# IMTOnlineArray::AddCopy

Add copies of the connection record objects in an array.

C++
    
    
    MTAPIRES  IMTOnlineArray::AddCopy(
       const IMTOnlineArray*  array      // Added connection record array
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.AddCopy(
       CIMTOnlineArray        array      // Added connection record array
       )

### Parameters

**array**  
[in] Connection record array object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the client record objects belonging to the array object, and inserts them at the end of the current array.
