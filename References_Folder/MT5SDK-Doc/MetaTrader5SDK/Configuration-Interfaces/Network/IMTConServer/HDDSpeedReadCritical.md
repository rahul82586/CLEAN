[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HDDSpeedReadCritical

[Previous](HDDSpeedRead.md) | [Next](HDDSpeedWrite.md)

# IMTConServer::HDDSpeedReadCritical

Get the critical speed of data reading from the hard disk.

C++
    
    
    UINT  IMTConServer::HDDSpeedReadCritical()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.HDDSpeedReadCritical()

Python (Manager API)
    
    
    MTConServer.HDDSpeedReadCritical

### Return Value

The critical speed of data reading from the hard disk in Mb/sec.

### Note

The critical level is strictly defined. This method allows to respond to the critical state of the system.
