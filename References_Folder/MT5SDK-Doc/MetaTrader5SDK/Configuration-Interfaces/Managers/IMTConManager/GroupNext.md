[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / GroupNext

[Previous](GroupTotal.md) | [Next](AccessAdd.md)

# IMTConManager::GroupNext

Get [a group](../../Groups.md) processed by the manager, at a specified position in the list.

C++
    
    
    LPCWSTR  IMTConManager::GroupNext(
       const UINT  pos      // Position of the group
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConManager.GroupNext(
       uint        pos      // Position of the group
       )

Python (Manager API)
    
    
    MTConManager.GroupNext(
       pos         # Position of the group
       )
    
    
    MTConManager.GroupGet()

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

### Return Value

If successful, it returns a pointer to a string with a path to the group. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConManager](../IMTConManager.md) object.
