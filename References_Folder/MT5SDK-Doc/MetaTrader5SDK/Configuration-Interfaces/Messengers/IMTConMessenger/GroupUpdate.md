[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / GroupUpdate

[Previous](GroupAdd.md) | [Next](GroupDelete.md)

# IMTConMessenger::GroupUpdate

Change the group of accounts for which the messenger is used.

C++
    
    
    MTAPIRES  IMTConMessenger::GroupUpdate(
       const UINT                     pos,      // Group position
       const IMTConMessengerGroup*    group     // Group object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.GroupUpdate(
       uint                           pos,      // Group position
       CIMTConMessengerGroup          group     // Group object
       )

Python
    
    
    MTConMessenger.GroupUpdate(
       pos,                           # Group position
       group                          # Group object
       )
    
    
    MTConMessenger.GroupSet(
       group_list                     # List of groups
       )

### Parameters

**pos**  
[in] Position of a group in the list, starting with 0.

**group**  
[in] Account group objectIMTConMessengerGroup.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
