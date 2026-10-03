[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HDDFragments

[Previous](HDDFreeCritical.md) | [Next](HDDFragmentsCritical.md)

# IMTConServer::HDDFragments

Gets the current level of fragmentation of server files.

C++
    
    
    UINT  IMTConServer::HDDFragments()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.HDDFragments()

Python (Manager API)
    
    
    MTConServer.HDDFragments

### Return Value

The current level of fragmentation of server files in percentage.

### Note

The fragmentation level is calculated only for the files within the server installation directory.
