[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTConGroupArray::UpdateCopy

Update a group at the specified position of an array by copying the parameters of a passed group object.

C++
    
    
    MTAPIRES  IMTConGroupArray::UpdateCopy(
       const UINT           pos,      // Position
       const IMTConGroup*   record    // Group object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupArray.UpdateCopy(
       uint                 pos,      // Position
       CIMTConGroup         record    // Group object
       )

### Parameters

**pos**  
[in] Group position in the array, starting with 0.

**record**  
[in] Group object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method copies the 'record' object to the parameter object at the specified array position.
