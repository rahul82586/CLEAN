[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTConGroupArray::Delete

Delete a group object by position.

C++
    
    
    MTAPIRES  IMTConGroupArray::Delete(
       const UINT  pos      // Group position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupArray.Delete(
       uint        pos      // Group position
       )

### Parameters

**pos**  
[in] Group position in the array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The deleted object will be automatically released by [IMTConGroup::Release](../IMTConGroup/Release.md) method call.
