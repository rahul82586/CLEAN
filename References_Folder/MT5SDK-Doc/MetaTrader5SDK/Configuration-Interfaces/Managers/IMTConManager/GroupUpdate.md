[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / GroupUpdate

[Previous](GroupAdd.md) | [Next](GroupShift.md)

# IMTConManager::GroupUpdate

Modify [a group of accounts](../../Groups.md), which is processed by the manager, at the specified position in the list.

C++
    
    
    MTAPIRES  IMTConManager::GroupUpdate(
       const UINT  pos,      // Position of the group
       LPCWSTR     path      // Path to the group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.GroupUpdate(
       uint        pos,      // Position of the group
       string      path      // Path to the group
       )

Python (Manager API)
    
    
    MTConManager.GroupUpdate(
       pos,        # Position of the group
       path        # Path to the group
       )
    
    
    MTConManager.GroupSet(
       path_list   # A list of paths
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

**path**  
[in] The updated path to a group in accordance with the hierarchy of groups.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The value of [IMTConGroup::Group](../../Groups/IMTConGroup/Group.md) is used as the path to the group.
