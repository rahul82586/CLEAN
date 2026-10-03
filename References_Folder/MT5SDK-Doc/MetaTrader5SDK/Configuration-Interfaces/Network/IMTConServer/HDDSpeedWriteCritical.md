[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HDDSpeedWriteCritical

[Previous](HDDSpeedWrite.md) | [Next](ConnectsMax.md)

# IMTConServer::HDDSpeedWriteCritical

Get the critical speed of information writing on the hard disk.

C++
    
    
    UINT  IMTConServer::HDDSpeedWriteCritical()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.HDDSpeedWriteCritical()

Python (Manager API)
    
    
    MTConServer.HDDSpeedWriteCritical

### Return Value

The critical speed of information writing on the hard disk in Mb/sec.

### Note

The critical level is strictly defined. This method allows to respond to the critical state of the system.
