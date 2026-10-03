[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / AccessDelete

[Previous](AccessUpdate.md) | [Next](AccessShift.md)

# IMTConManager::AccessDelete

Delete a range of IP addresses, from which a manager is allowed to connect to the platform, based on its position in the list.

C++
    
    
    MTAPIRES  IMTConManager::AccessDelete(
       const UINT  pos      // Position of a range of addresses
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.AccessDelete(
       uint        pos      // Position of a range of addresses
       )

Python (Manager API)
    
    
    MTConManager.AccessDelete(
       pos         # Position of a range of addresses
       )

### Parameters

**pos**  
[in] Position of a range of addresses in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
