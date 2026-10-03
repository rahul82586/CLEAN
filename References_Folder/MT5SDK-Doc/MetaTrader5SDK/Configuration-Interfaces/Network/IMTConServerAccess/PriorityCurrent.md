[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / PriorityCurrent

[Previous](Priority.md) | [Next](AccessFlags.md)

# IMTConServerAccess::PriorityCurrent

Get the current priority of the Access Server.

C++
    
    
    UINT  IMTConServerAccess::PriorityCurrent()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerAccess.PriorityCurrent()

Python (Manager API)
    
    
    MTConServerAccess.PriorityCurrent

### Return Value

The current priority of the Access Server.

### Note

The current priority of an Access Server is calculated based on its [base priority](Priority.md) and the current server load.
