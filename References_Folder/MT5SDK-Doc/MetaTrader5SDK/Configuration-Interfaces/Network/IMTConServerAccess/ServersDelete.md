[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / ServersDelete

[Previous](ServersShift.md) | [Next](ServersClear.md)

# IMTConServerAccess::ServersDelete

Delete a trade server, the connection to which is implemented through this Access Server, from the list.

C++
    
    
    MTAPIRES  IMTConServerAccess::ServersDelete(
       const UINT  pos      // Position of the trade server
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.ServersDelete(
       uint        pos      // Position of the trade server
       )

Python (Manager API)
    
    
    MTConServerAccess.ServersDelete(
       pos         # Position of the trade server
       )

### Parameters

**pos**  
[in] Position of the trade server in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
