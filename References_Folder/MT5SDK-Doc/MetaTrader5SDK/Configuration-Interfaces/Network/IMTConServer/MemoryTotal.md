[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / MemoryTotal

[Previous](CPUUsageCritical.md) | [Next](MemoryFree.md)

# IMTConServer::MemoryTotal

Get the total amount of available RAM.

C++
    
    
    UINT  IMTConServer::MemoryTotal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.MemoryTotal()

Python (Manager API)
    
    
    MTConServer.MemoryTotal

### Return Value

The total amount of RAM in megabytes.

### Note

The variable is measured once a minute. The state can be different between measurements.
