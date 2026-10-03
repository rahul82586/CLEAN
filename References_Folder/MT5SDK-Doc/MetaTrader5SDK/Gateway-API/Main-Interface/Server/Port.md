[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Server](../Server.md) / Port

[Previous](IP.md) | [Next](Connections.md)

# IMTGatewayAPI::ServerPort

Get the number of the port launched for the connection to Gateway API.

C++
    
    
    UINT  IMTGatewayAPI::ServerPort()

.NET
    
    
    uint  CIMTGatewayAPI.ServerPort()

### Return Value

Server port number. In case several addresses (for example: address1:port1,address2:port2) have been specified via [IMTGatewayAPI::Start](Start.md) method, this method will return the port of the first address (port1).
