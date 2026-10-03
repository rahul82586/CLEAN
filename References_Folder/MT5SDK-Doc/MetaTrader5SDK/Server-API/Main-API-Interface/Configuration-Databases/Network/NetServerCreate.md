[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerCreate

[Previous](../Network.md) | [Next](NetServerClusterStateCreate.md)

# IMTServerAPI::NetServerCreate

Create an object of configuration of the platform components.
    
    
    IMTConServer*  IMTServerAPI::NetServerCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConServer](../../../../Configuration-Interfaces/Network/IMTConServer.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConServer::Release](../../../../Configuration-Interfaces/Network/IMTConServer/Release.md) method of this object.
