[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HDDFree

[Previous](HDDTotal.md) | [Next](HDDFreeCritical.md)

# IMTConServer::HDDFree

Get the amount of free memory on the hard disk.

C++
    
    
    UINT  IMTConServer::HDDFree()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.HDDFree()

Python (Manager API)
    
    
    MTConServer.HDDFree

### Return Value

Free memory on the hard disk in megabytes.

### Note

The variable is measured once a minute. The state can be different between measurements.
