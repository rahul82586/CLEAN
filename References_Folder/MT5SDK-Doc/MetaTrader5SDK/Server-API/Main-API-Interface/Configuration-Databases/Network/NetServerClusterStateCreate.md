[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerClusterStateCreate

[Previous](NetServerCreate.md) | [Next](NetServerRangeCreate.md)

# IMTServerAPI::NetServerClusterStateCreate

Create the network connection status object.
    
    
    IMTConClusterState*  IMTServerAPI::NetServerClusterStateCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTConClusterState](../../../../Configuration-Interfaces/Network/IMTConClusterState.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConClusterState::Release](../../../../Configuration-Interfaces/Network/IMTConClusterState/Release.md) method of this object.
