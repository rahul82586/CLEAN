[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / GroupAdd

[Previous](Right.md) | [Next](GroupUpdate.md)

# IMTConManager::GroupAdd

Add [a group of accounts](../../Groups.md) that the manager will process.

C++
    
    
    MTAPIRES  IMTConManager::GroupAdd(
       LPCWSTR  path      // Path to the group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.GroupAdd(
       string   path      // Path to the group
       )

Python (Manager API)
    
    
    MTConManager.GroupAdd(
       path     # Path to the group
       )

### Parameters

**path**  
[in] Path to a group in accordance with the hierarchy of groups.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The value of [IMTConGroup::Group](../../Groups/IMTConGroup/Group.md) is used as the path to the group.
