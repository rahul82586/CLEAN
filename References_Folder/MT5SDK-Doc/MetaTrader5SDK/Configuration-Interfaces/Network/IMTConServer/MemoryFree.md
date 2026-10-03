[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / MemoryFree

[Previous](MemoryTotal.md) | [Next](MemoryFreeMin.md)

# IMTConServer::MemoryFree

Get the amount of free RAM.

C++
    
    
    UINT  IMTConServer::MemoryFree()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.MemoryFree()

Python (Manager API)
    
    
    MTConServer.MemoryFree

### Return Value

The amount of free memory in megabytes.

### Note

The variable is measured once a minute. The state can be different between measurements.
