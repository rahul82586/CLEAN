[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerClusterStateCreate

[Previous](NetServerAddressRangeCreate.md) | [Next](NetServerBackupFolderCreate.md)

# IMTAdminAPI::NetServerClusterStateCreate

Create a network connection status object.

C++
    
    
    IMTConClusterState*  IMTAdminAPI::NetServerClusterStateCreate()

.NET
    
    
    CIMTConClusterState  CIMTAdminAPI.NetServerClusterStateCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTConClusterState](../../../../Configuration-Interfaces/Network/IMTConClusterState.md) interface. Returns NULL on failure.

### Note

The created object must be destroyed by calling the [IMTConClusterState::Release](../../../../Configuration-Interfaces/Network/IMTConClusterState/Release.md) method of this object.
