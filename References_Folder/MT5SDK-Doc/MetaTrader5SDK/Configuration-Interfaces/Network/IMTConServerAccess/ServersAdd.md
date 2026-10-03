[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / ServersAdd

[Previous](BindingsNext.md) | [Next](ServersUpdate.md)

# IMTConServerAccess::ServersAdd

Add a trade server, the connection to which will be implemented through this Access Server.

C++
    
    
    MTAPIRES  IMTConServerAccess::ServersAdd(
       const UINT64  server_id      // ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.ServersAdd(
       ulong         server_id      // ID
       )

Python (Manager API)
    
    
    MTConServerAccess.ServersAdd(
       server_id     # ID
       )

### Parameters

**server_id**  
[in] Trade server ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
