[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / GroupShift

[Previous](GroupUpdate.md) | [Next](GroupDelete.md)

# IMTConManager::GroupShift

Move [a group of accounts](../../Groups.md), which is processed by the manager, in the list of groups.

C++
    
    
    MTAPIRES  IMTConManager::GroupShift(
       const UINT  pos,       // Position of the group
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.GroupShift(
       uint        pos,       // Position of the group
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConManager.GroupShift(
       pos,        # Position of the group
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

**shift**  
[in] Shift of a group relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
