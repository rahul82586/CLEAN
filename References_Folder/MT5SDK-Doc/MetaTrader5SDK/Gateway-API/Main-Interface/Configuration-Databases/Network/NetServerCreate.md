[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerCreate

[Previous](../Network.md) | [Next](NetServerRangeCreate.md)

# IMTGatewayAPI::NetServerCreate

Create an object of configuration of the platform components.

C++
    
    
    IMTConServer*  IMTGatewayAPI::NetServerCreate()

.NET
    
    
    CIMTConServer  CIMTGatewayAPI.NetServerCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConServer](../../../../Configuration-Interfaces/Network/IMTConServer.md) interface. In case of failure, it returns Null.

### Note

The created object must be deleted by calling the [IMTConServer::Release](../../../../Configuration-Interfaces/Network/IMTConServer/Release.md) method of this object.
