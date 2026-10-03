[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / MemoryFreeCritical

[Previous](MemoryFreeMin.md) | [Next](HDDTotal.md)

# IMTConServer::MemoryFreeCritical

Get the critical level of free RAM.

C++
    
    
    UINT  IMTConServer::MemoryFreeCritical()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.MemoryFreeCritical()

Python (Manager API)
    
    
    MTConServer.MemoryFreeCritical

### Return Value

The critical amount of free memory in megabytes.

### Note

The critical level is strictly defined. This method allows to respond to the critical state of the system.
