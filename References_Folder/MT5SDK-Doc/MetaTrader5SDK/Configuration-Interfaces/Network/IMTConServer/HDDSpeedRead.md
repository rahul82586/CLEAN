[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HDDSpeedRead

[Previous](HDDFragmentsCritical.md) | [Next](HDDSpeedReadCritical.md)

# IMTConServer::HDDSpeedRead

Get the speed of data reading from the hard disk.

C++
    
    
    UINT  IMTConServer::HDDSpeedRead()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.HDDSpeedRead()

Python (Manager API)
    
    
    MTConServer.HDDSpeedRead

### Return Value

The speed of data reading from the hard disk in Mb/sec.

### Note

Disk performance is measured once a day, during [platform optimization time](ServiceTime.md).
