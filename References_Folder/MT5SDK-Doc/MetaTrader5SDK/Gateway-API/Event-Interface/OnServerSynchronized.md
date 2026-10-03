[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnServerSynchronized

[Previous](OnServerDisconnect.md) | [Next](OnServerSymbolAdd.md)

# IMTGatewaySink::OnServerSynchronized

A handler of the event of data synchronization between Gateway API and one of the MetaTrader 5 platform (server) components.

C++
    
    
    virtual void  IMTGatewaySink::OnServerSynchronized(
       LPCWSTR       address,     // IP address
       const UINT    type,        // component type
       const UINT64  id           // server ID
       )

.NET
    
    
    virtual void  CIMTGatewaySink.OnServerSynchronized(
       string        address,     // IP address
       uint          type,        // component type
       ulong         id           // server ID
       )

### Parameters

**address**  
[in] IP address of the platform component the synchronization has been performed with.

**type**  
[in] Type of the platform component the synchronization has been performed with. TheIMTGatewayAPI::CONNECT_TYPE_TRADE(trade server),IMTGatewayAPI::CONNECT_TYPE_HISTORY(history server) andIMTGatewayAPI::CONNECT_TYPE_BACKUP(backup server) values are used to pass the type.

**id**  
[in] ID of the server (IMTConServer::ID) the synchronization has been performed with. This parameter passes 0 when synchronizing with the history or backup server.

### Note

Use this handler if the gateway works with additional (not main) trade servers. When working only with the main trade server, it is sufficient to use [IMTGatewaySink::OnGatewayStart](OnGatewayStart.md).
