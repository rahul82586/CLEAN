[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayCreate

[Previous](../Gateways.md) | [Next](GatewayModuleCreate.md)

# IMTServerAPI::GatewayCreate

Create an object of the gateway configuration.
    
    
    IMTConGateway*  IMTServerAPI::GatewayCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConGateway](../../../../Configuration-Interfaces/Gateways/IMTConGateway.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConGateway::Release](../../../../Configuration-Interfaces/Gateways/IMTConGateway/Release.md) method of this object.
