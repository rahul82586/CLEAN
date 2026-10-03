[🏠 Document Start](../README.md) / [Manager API](README.md) / Interface of Events

[Previous](Dealer-Interface/OnDealerAnswer.md) | [Next](Interface-of-Manager-API-Events/Interface-of-Events-OnConnect.md)

# Manager API Events Interface — IMTManagerSink

IMTManagerSink interface contains the following handlers:

Method | Purpose  
---|---  
[OnConnect](Interface-of-Manager-API-Events/Interface-of-Events-OnConnect.md) | A handler that notifies of establishing/restoring a connection between the manager or administrator terminal and the server.  
[OnDisconnect](Interface-of-Manager-API-Events/Interface-of-Events-OnDisconnect.md) | A handler that notifies of loss of connection between the manager or administrator terminal and the server.  
[OnTradeAccountSet](Interface-of-Manager-API-Events/Interface-of-Events-OnTradeAccountSet.md) | This handler receives [IMTManagerAPI::TradeAccountSet](Manager-Interface/Trade-Activity/Monitoring-Account-States/TradeAccountSet.md) method execution result, as well as the final status of a client entry (after the passed changes have been applied).
