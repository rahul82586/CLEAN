[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / TradeServer

[Previous](Critical.md) | [Next](HistoryServer.md)

# IMTConServer::TradeServer

The interface of the Trade Server.

C++
    
    
    IMTConServerTrade*  IMTConServer::TradeServer()

.NET (Gateway/Manager API)
    
    
    CIMTConServerTrade  CIMTConServer.TradeServer()

Python (Manager API)
    
    
    MTConServer.TradeServer()

### Return Value

It returns a pointer to the object that implements the [IMTConServerTrade](../IMTConServerTrade.md) interface. In case of failure, it returns NULL.

### Note

The server type [IMTConServer::Type()](Type.md) defines what specific parameters the server has.
