[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTConGroupArray::Update

Update a group at the specified position of an array.

C++
    
    
    MTAPIRES  IMTConGroupArray::Update(
       const UINT     pos,       // Position
       IMTConGroup*   record     // Group object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupArray.Update(
       uint           pos,       // Position
       CIMTConGroup  record      // Group object
       )

### Parameters

**pos**  
[in] Group position in the array, starting with 0.

**record**  
[in]IMTConGroupgroup object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTConGroupArray::Update method deletes the previous element (by calling [IMTConGroup::Release](../IMTConGroup/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by the array object. Thus, when deleting an array object (by calling IMTConGroupArray::Release), an earlier inserted object will be automatically deleted.
