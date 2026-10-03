[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / HistoryServer

[Previous](TradeServer.md) | [Next](AccessServer.md)

# IMTConServer::HistoryServer

The interface of the History Server.

C++
    
    
    IMTConServerHistory*  IMTConServer::HistoryServer()

.NET (Gateway/Manager API)
    
    
    CIMTConServerHistory  CIMTConServer.HistoryServer()

Python (Manager API)
    
    
    MTConServer.HistoryServer()

### Return Value

It returns a pointer to the object that implements the [IMTConServerHistory](../IMTConServerHistory.md) interface. In case of failure, it returns NULL.

### Note

The server type [IMTConServer::Type()](Type.md) defines what specific parameters the server has.
