[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HDDFreeCritical

[Previous](HDDFree.md) | [Next](HDDFragments.md)

# IMTConServer::HDDFreeCritical

Get the critical amount of free memory on the hard disk.

C++
    
    
    UINT  IMTConServer::HDDFreeCritical()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.HDDFreeCritical()

Python (Manager API)
    
    
    MTConServer.HDDFreeCritical

### Return Value

Critical amount of free memory on the hard disk in megabytes.

### Note

The critical level is strictly defined. This method allows to respond to the critical state of the system.
