[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayModuleCreate

[Previous](GatewayCreate.md) | [Next](GatewayParamCreate.md)

# IMTServerAPI::GatewayModuleCreate

Create an object of configuration of the gateway module.
    
    
    IMTConGatewayModule*  IMTServerAPI::GatewayModuleCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConGatewayModule](../../../../Configuration-Interfaces/Gateways/IMTConGatewayModule.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConGatewayModule::Release](../../../../Configuration-Interfaces/Gateways/IMTConGatewayModule/Release.md) method of this object.
