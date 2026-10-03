[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / Server

[Previous](Mailbox.md) | [Next](LimitLogs.md)

# IMTConManager::Server

Get the ID of the trade server, to which the manager belongs.

C++
    
    
    UINT64  IMTConManager::Server()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConManager.Server()

Python (Manager API)
    
    
    MTConManager.Server

### Return Value

The ID of the trade server, to which the manager belongs.

### Note

Binding of a manager to a server is defined by the binding of a group, in which the manager account is created.
