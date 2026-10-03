[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / ServersClear

[Previous](ServersDelete.md) | [Next](ServersTotal.md)

# IMTConServerAntiDDoS::ServersClear

Clear the list of trade servers, the connection to which is implemented through this Anti DDoS server.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::ServersClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAntiDDoS.ServersClear()

Python (Manager API)
    
    
    MTConServerAntiDDoS.ServersClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method clears the list of trade servers in the Anti-DDoS server settings.
