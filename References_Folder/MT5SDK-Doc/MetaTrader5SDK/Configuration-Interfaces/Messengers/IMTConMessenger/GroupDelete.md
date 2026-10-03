[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / GroupDelete

[Previous](GroupUpdate.md) | [Next](GroupClear.md)

# IMTConMessenger::GroupDelete

Delete the group of accounts for which the messenger is used.

C++
    
    
    MTAPIRES  IMTConMessenger::GroupDelete(
       const UINT  pos      // Group position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.GroupDelete(
       uint        pos      // Group position
       )

Python
    
    
    MTConMessenger.GroupDelete(
       pos         # Group position
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
