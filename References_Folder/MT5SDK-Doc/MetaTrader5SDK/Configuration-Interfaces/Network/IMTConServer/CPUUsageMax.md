[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / CPUUsageMax

[Previous](CPUTotal.md) | [Next](CPUUsageCritical.md)

# IMTConServer::CPUUsageMax

Get the maximum level of CPU usage.

C++
    
    
    UINT  IMTConServer::CPUUsageMax()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.CPUUsageMax()

Python (Manager API)
    
    
    MTConServer.CPUUsageMax

### Return Value

The maximum level of CPU usage in percent, registered in the past 24 hours.
