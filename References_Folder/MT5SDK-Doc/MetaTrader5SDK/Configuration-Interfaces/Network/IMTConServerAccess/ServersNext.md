[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / ServersNext

[Previous](ServersTotal.md) | [Next](../IMTConServerAntiDDoS.md)

# IMTConServerAccess::ServersNext

Get a trade server, the connection to which is implemented through this Access Server, by the index.

C++
    
    
    UINT64  IMTConServerAccess::ServersNext(
       const UINT  pos      // Position of the trade server
       )  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConServerAccess.ServersNext(
       uint        pos      // Position of the trade server
       )

Python (Manager API)
    
    
    MTConServerAccess.ServersNext(
       pos         # Position of the trade server
       )

### Parameters

**pos**  
[in] Position of the trade server in the list, starting with 0.

### Return Value

Trade server ID.
