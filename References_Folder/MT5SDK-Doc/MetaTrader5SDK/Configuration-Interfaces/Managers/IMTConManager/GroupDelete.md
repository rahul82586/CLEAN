[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / GroupDelete

[Previous](GroupShift.md) | [Next](GroupTotal.md)

# IMTConManager::GroupDelete

Delete a group of accounts processed by the manager, by its index

C++
    
    
    MTAPIRES  IMTConManager::GroupDelete(
       const UINT  pos      // Position of the group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.GroupDelete(
       uint        pos      // Position of the group
       )

Python (Manager API)
    
    
    MTConManager.GroupDelete(
       pos         # Position of the group
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
