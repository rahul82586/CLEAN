[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Critical

[Previous](Max.md) | [Next](TradeServer.md)

# IMTConServer::NetworkCritical

Get the critical level of network usage.

C++
    
    
    UINT  IMTConServer::NetworkCritical()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.NetworkCritical()

Python (Manager API)
    
    
    MTConServer.NetworkCritical

### Return Value

The critical level of network usage in Kbps.

### Note

The value is based on the total incoming and outgoing traffic measured on the [selected network interface](AdaptersCurrent.md). This includes the traffic of all programs running on the server machine.
