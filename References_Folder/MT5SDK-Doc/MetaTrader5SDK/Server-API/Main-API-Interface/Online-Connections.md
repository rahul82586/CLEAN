[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Main API Interface](../Main-API-Interface.md) / Online Connections

[Previous](Users/UserAccountGet.md) | [Next](Online-Connections/OnlineCreate.md)

# Online Connections

MetaTrader 5 Server API provides functions for receiving data on the current connections to the trade server. All types of connection are considered, including client, manager and API ones with the exception of the cluster components' (platform servers') connections.

Function | Purpose  
---|---  
[OnlineCreate](Online-Connections/OnlineCreate.md) | Create connection record object.  
[OnlineCreateArray](Online-Connections/OnlineCreateArray.md) | Create connection record array object.  
[OnlineTotal](Online-Connections/OnlineTotal.md) | Get the total amount of the current connections to the trade server.  
[OnlineNext](Online-Connections/OnlineNext.md) | Get connection record by index.  
[OnlineGet](Online-Connections/OnlineGet.md) | Get connection record by login.  
[OnlineDisconnect](Online-Connections/OnlineDisconnect.md) | Forced disconnection of a client from the server.  
[OnlineDisconnectBatch](Online-Connections/OnlineDisconnectBatch.md) | Forced disconnection of multiple clients from the server.  
[OnlineDisconnectBatchArray](Online-Connections/OnlineDisconnectBatchArray.md) | Forced disconnection of multiple clients from the server.
