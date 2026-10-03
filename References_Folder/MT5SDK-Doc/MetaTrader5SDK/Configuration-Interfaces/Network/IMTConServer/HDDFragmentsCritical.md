[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HDDFragmentsCritical

[Previous](HDDFragments.md) | [Next](HDDSpeedRead.md)

# IMTConServer::HDDFragmentsCritical

Gets the critical level of fragmentation of server files.

C++
    
    
    UINT  IMTConServer::HDDFragmentsCritical()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.HDDFragmentsCritical()

Python (Manager API)
    
    
    MTConServer.HDDFragmentsCritical

### Return Value

The critical level of fragmentation of server files in percentage.

### Note

The critical level is strictly defined. This method allows to respond to the critical state of the system.
