[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HDDTotal

[Previous](MemoryFreeCritical.md) | [Next](HDDFree.md)

# IMTConServer::HDDTotal

Get the total volume of the hard disk.

C++
    
    
    UINT  IMTConServer::HDDTotal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.HDDTotal()

Python (Manager API)
    
    
    MTConServer.HDDTotal

### Return Value

Total volume of a hard disk in megabytes.

### Note

The variable is measured once a minute. The state can be different between measurements.
