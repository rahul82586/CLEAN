[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTConGroupArray::AddCopy

Add a copy of a group object to the end of an array.

C++
    
    
    MTAPIRES  IMTConGroupArray::AddCopy(
       const IMTConGroup*   record    // Group to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupArray.AddCopy(
       CIMTConGroup         record    // Group to be added
       )

### Parameters

**record**  
[in]IMTConGroupgroup object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'record' object and places it to the end of the array.

# IMTConGroupArray::AddCopy

Add copies of group objects to an array.

C++
    
    
    MTAPIRES  IMTConGroupArray::AddCopy(
       const IMTConGroupArray*   array      // Group array to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupArray.AddCopy(
       CIMTConGroupArray         array      // Group array to be added
       )

### Parameters

**array**  
[in] Group array objectIMTConGroupArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of objects belonging to the 'array' object, and inserts them at the end of the current array.
