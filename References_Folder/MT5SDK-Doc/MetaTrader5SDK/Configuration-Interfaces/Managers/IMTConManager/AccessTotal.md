[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / AccessTotal

[Previous](AccessShift.md) | [Next](AccessNext.md)

# IMTConManager::AccessTotal

Get the number of ranges of IP addresses, from which a manager is allowed to connect to the platform.

C++
    
    
    UINT  IMTConManager::AccessTotal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConManager.AccessTotal()

Python (Manager API)
    
    
    MTConManager.AccessTotal()

### Return Value

The number of ranges of IP addresses.
