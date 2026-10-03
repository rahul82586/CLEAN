[🏠 Document Start](../README.md) / [Gateway API](README.md) / Event Interface

[Previous](Main-Interface/User-Settings/SettingsGet.md) | [Next](Event-Interface/OnServerDisconnect.md)

# IMTGatewaySink Interface

IMTGatewaySink interface is used to notify on the events happening at a trading platform. It also allows to manage a platform connection to Gateway API.

IMTGatewaySink interface contains the following methods:

Method | Purpose  
---|---  
[OnServerDisconnect](Event-Interface/OnServerDisconnect.md) | A handler of the event of the end of connection to one of the MetaTrader 5 platform components (server).  
[OnServerSynchronized](Event-Interface/OnServerSynchronized.md) | A handler of the event of data synchronization between Gateway API and one of the MetaTrader 5 platform (server) components.  
[OnServerSymbolAdd](Event-Interface/OnServerSymbolAdd.md) | A handler of the event of symbol adding.  
[OnServerSymbolDelete](Event-Interface/OnServerSymbolDelete.md) | A handler of the event of symbol removal.  
[OnGatewayConfig](Event-Interface/OnGatewayConfig.md) | A handler of the event of passing a gateway/data feed own configuration from a history server connected to it.  
[OnGatewayStart](Event-Interface/OnGatewayStart.md) | A handler of the following event: Gateway API is synchronized with the platform and is ready for work.  
[OnGatewayStop](Event-Interface/OnGatewayStop.md) | OnGatewayStart inverse events hadler. Notifies on the fact that Gateway API is not synchronized with the platform and not ready for work.  
[OnGatewayShutdown](Event-Interface/OnGatewayShutdown.md) | A handler of the event notifying about the trading platform shutdown or gateway/data feed disconnection.  
[OnGatewayAccountAnswer](Event-Interface/OnGatewayAccountAnswer.md) | A handler of the event of requesting information about a client from MetaTrader 5 platform.  
[OnGatewayAccountSet](Event-Interface/OnGatewayAccountSet.md) | A handler of the event of modifying information about a client via [IMTGatewayAPI::GatewayAccountSet](Main-Interface/Synchronizing-Trading-Data/GatewayAccountSet.md) method.  
[OnDealerLock](Event-Interface/OnDealerLock.md) | A handler of the event of capturing (blocking) of a successive trade request from a requests queue.  
[OnDealerAnswer](Event-Interface/OnDealerAnswer.md) | A handler of the event notifying on a request confirmation or execution result.  
[HookServerConnect](Event-Interface/HookServerConnect.md) | The hook for managing MetaTrader 5 platform components connections to Gateway API.  
[HookGatewayPositionsRequest](Event-Interface/HookGatewayPositionsRequest.md) | The hook for receiving states of trading accounts used by the gateway to operate in an external system.  
[HookGatewayPositionsCheck](Event-Interface/HookGatewayPositionsCheck.md) | Hook for positions verification. This method is reserved for future use.  
[HookGatewayOrdersRequest](Event-Interface/HookGatewayOrdersRequest.md) | The hook for receiving the state of the client's current pending orders in an external trading system.  
[HookGatewayAccountRequest](Event-Interface/HookGatewayAccountRequest.md) | The hook for synchronizing client's trading data with an external trading system.
