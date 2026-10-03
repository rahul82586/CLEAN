[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerCreate

[Previous](../Network.md) | [Next](NetServerRangeCreate.md)

# IMTAdminAPI::NetServerCreate

Create an object of configuration of the platform components.

C++
    
    
    IMTConServer*  IMTAdminAPI::NetServerCreate()

.NET
    
    
    CIMTConServer  CIMTAdminAPI.NetServerCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConServer](../../../../Configuration-Interfaces/Network/IMTConServer.md) interface. In case of failure, it returns Null.

### Note

The created object must be deleted by calling the [IMTConServer::Release](../../../../Configuration-Interfaces/Network/IMTConServer/Release.md) method of this object.
