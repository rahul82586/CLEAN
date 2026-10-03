[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / AccessUpdate

[Previous](AccessAdd.md) | [Next](AccessDelete.md)

# IMTConManager::AccessUpdate

Modifies a range of IP addresses, from which a manager is allowed to connect to the platform, based on its position in the list.

C++
    
    
    MTAPIRES  IMTConManager::AccessUpdate(
       const UINT                  pos,        // Position of the range
       const IMTConManagerAccess*  access      // An object of the range of addresses
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.AccessUpdate(
       uint                        pos,        // Position of the range
       CIMTConManagerAccess        access      // An object of the range of addresses
       )

Python (Manager API)
    
    
    MTConManager.AccessUpdate(
       pos,                        # Position of the range
       access                      # An object of the range of addresses
       )
    
    
    MTConManager.AccessSet(
       access_list                 # A list of address ranges
       )

### Parameters

**pos**  
[in] Position of a range of addresses in the list, starting with 0.

**access**  
[in] An object of the range of addresses.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
