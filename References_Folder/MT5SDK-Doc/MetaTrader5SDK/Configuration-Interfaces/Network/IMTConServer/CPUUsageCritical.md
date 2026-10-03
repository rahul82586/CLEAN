[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / CPUUsageCritical

[Previous](CPUUsageMax.md) | [Next](MemoryTotal.md)

# IMTConServer::CPUUsageCritical

Get the critical level of CPU usage.

C++
    
    
    UINT  IMTConServer::CPUUsageCritical()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.CPUUsageCritical()

Python (Manager API)
    
    
    MTConServer.CPUUsageCritical

### Return Value

The critical level of CPU usage in percentage.

### Note

The critical level is strictly defined. This method allows to respond to the critical state of the system.
