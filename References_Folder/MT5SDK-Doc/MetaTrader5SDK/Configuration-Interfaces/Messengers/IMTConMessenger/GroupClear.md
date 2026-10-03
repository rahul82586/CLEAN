[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / GroupClear

[Previous](GroupDelete.md) | [Next](GroupShift.md)

# IMTConMessenger::GroupClear

Clear the list of groups for which the messenger is used.

C++
    
    
    MTAPIRES  IMTConMessenger::GroupClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.GroupClear()

Python
    
    
    MTConMessenger.GroupClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method deletes from the list all groups for which the messenger is used.
