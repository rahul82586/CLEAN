[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / ServersDelete

[Previous](ServersShift.md) | [Next](ServersClear.md)

# IMTConServerAntiDDoS::ServersDelete

Delete from the list a trade server, the connection to which is implemented through this Anti DDoS server.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::ServersDelete(
       const UINT  pos      // The position of the trade server
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAntiDDoS.ServersDelete(
       uint        pos      // The position of the trade server
       )

Python (Manager API)
    
    
    MTConServerAntiDDoS.ServersDelete(
       pos         # The position of the trade server
       )

### Parameters

**pos**  
[in] Position of the trade server in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
