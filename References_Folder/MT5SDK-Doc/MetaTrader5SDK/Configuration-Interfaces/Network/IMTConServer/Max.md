[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Max

[Previous](ConnectsCritical.md) | [Next](Critical.md)

# IMTConServer::NetworkMax

Get the maximum level of network usage reached during the day.

C++
    
    
    UINT  IMTConServer::NetworkMax()

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.NetworkMax()

Python (Manager API)
    
    
    MTConServer.NetworkMax

### Return Value

The maximum level of network usage in Kbps, registered in the past 24 hours.

### Note

The value is based on the total incoming and outgoing traffic measured on the [selected network interface](AdaptersCurrent.md). This includes the traffic of all programs running on the server machine.
