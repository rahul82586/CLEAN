[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerRangeCreate

[Previous](NetServerClusterStateCreate.md) | [Next](NetServerAddressRangeCreate.md)

# IMTServerAPI::NetServerRangeCreate

Create an object of the range of orders, deals or accounts.
    
    
    IMTConServerRange*  IMTServerAPI::NetServerRangeCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConServerRange](../../../../Configuration-Interfaces/Network/IMTConServerRange.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConServerRange::Release](../../../../Configuration-Interfaces/Network/IMTConServerRange/Release.md) method of this object.
