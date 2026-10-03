[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Connection to the Server](../Connection-to-the-Server.md) / ProxySet

[Previous](Unsubscribe.md) | [Next](../Operations-with-Connection.md)

# IMTAdminAPI::ProxySet

Set parameters of connection to the trading platform through a proxy server.

C++
    
    
    void  IMTAdminAPI::ProxySet(
       const MTProxyInfo&  proxy      // Proxy server
       )

.NET
    
    
    void  CIMTAdminAPI.ProxySet(
       MTProxyInfo         proxy      // Proxy server
       )

### Parameters

**proxy**  
[in] A reference to theMTProxyInfostructure that contains information about the parameters of connection via a proxy server.
