[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / ServersClear

[Previous](ServersDelete.md) | [Next](ServersTotal.md)

# IMTConServerAccess::ServersClear

Clear the list of trading servers connection to which is implemented through this Access Server.

C++
    
    
    MTAPIRES  IMTConServerAccess::ServersClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.ServersClear()

Python (Manager API)
    
    
    MTConServerAccess.ServersClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method clears the list of trading servers.
