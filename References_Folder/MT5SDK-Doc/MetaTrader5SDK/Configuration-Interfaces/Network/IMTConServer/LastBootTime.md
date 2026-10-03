[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / LastBootTime

[Previous](BuildDate.md) | [Next](Connected.md)

# IMTConServer::LastBootTime

Get the time of the last server boot.

C++
    
    
    INT64  IMTConServer::LastBootTime()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConServer.LastBootTime()

Python (Manager API)
    
    
    MTConServer.LastBootTime

### Return Value

The time of the last server boot in seconds that have elapsed since 01.01.1970.
