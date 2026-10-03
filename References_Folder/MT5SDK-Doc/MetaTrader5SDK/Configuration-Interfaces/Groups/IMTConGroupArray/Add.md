[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTConGroupArray::Add

Add a group object at the end of an array.

C++
    
    
    MTAPIRES  IMTConGroupArray::Add(
       IMTConGroup*    record    // group object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupArray.Add(
       CIMTConGrouop   record    // group object
       )

### Parameters

**record**  
[in]IMTConGroupgroup object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, control over the lifetime of the 'record' object is transferred to the array object. Thus, when deleting an array object (by calling [IMTConGroupArray::Release](Release.md)), an earlier inserted object will be automatically deleted.

# IMTConGroupArray::Add

Add an object of the groups array to the end of an array.

C++
    
    
    MTAPIRES  IMTConGroupArray::Add(
       IMTConGroupArray*  array      // Array of groups to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupArray.Add(
       CIMTConGroupArray  array      // Array of groups to be added
       )

### Parameters

**array**  
[in] Group array objectIMTConGroupArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers from the 'array' object to the end of the current array and clears the 'array' object.
