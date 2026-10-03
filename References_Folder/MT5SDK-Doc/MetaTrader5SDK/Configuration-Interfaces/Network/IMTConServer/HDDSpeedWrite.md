[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HDDSpeedWrite

[Previous](HDDSpeedReadCritical.md) | [Next](HDDSpeedWriteCritical.md)

# IMTConServer::HDDSpeedWrite

Get the speed of information writing on the hard disk.

C++
    
    
    UINT  IMTConServer::HDDSpeedWrite()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.HDDSpeedWrite()

Python (Manager API)
    
    
    MTConServer.HDDSpeedWrite

### Return Value

The speed of information writing on the hard disk in Mb/sec.

### Note

Disk performance is measured once a day, during [platform optimization time](ServiceTime.md).
