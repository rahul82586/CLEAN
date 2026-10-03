[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / MemoryFreeMin

[Previous](MemoryFree.md) | [Next](MemoryFreeCritical.md)

# IMTConServer::MemoryFreeMin

Get the minimum available amount of free RAM and virtual memory (swap file).

C++
    
    
    UINT  IMTConServer::MemoryFreeMin()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.MemoryFreeMin()

Python (Manager API)
    
    
    MTConServer.MemoryFreeMin

### Return Value

The minimum amount of free RAM and virtual memory in megabytes, registered in the past 24 hours.
