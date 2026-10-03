[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / ServersNext

[Previous](ServersTotal.md) | [Next](SourcesAdd.md)

# IMTConServerAntiDDoS::ServersNext

Get a trade server, the connection to which is implemented through this Anti DDoS server, by the index.

C++
    
    
    UINT64  IMTConServerAntiDDoS::ServersNext(
       const UINT  pos      // The position of the trade server
       )  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConServerAntiDDoS.ServersNext(
       uint        pos      // The position of the trade server
       )

Python (Manager API)
    
    
    MTConServerAntiDDoS.ServersNext(
       pos         # The position of the trade server
       )

### Parameters

**pos**  
[in] Position of the trade server in the list, starting with 0.

### Return Value

Trade server ID.
