[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTUserArray::AddCopy

Adds a copy of a client record object at the end of an array.

C++
    
    
    MTAPIRES  IMTUserArray::AddCopy(
       const IMTUser*  user      // The client record to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUserArray.AddCopy(
       CIMTUser        user      // The client record to be added
       )

### Parameters

**user**  
[in] An object of the client record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the user object and places it at the end of the array.

# IMTUserArray::AddCopy

Adds copies of the objects of client records to an array.

C++
    
    
    MTAPIRES  IMTUserArray::AddCopy(
       const IMTUserArray*  array      // An array of client records to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUserArray.AddCopy(
       CIMTUserArray        array      // An array of client records to be added
       )

### Parameters

**array**  
[in] An object of arrays of client records.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the client record objects belonging to the array object, and inserts them at the end of the current array.
