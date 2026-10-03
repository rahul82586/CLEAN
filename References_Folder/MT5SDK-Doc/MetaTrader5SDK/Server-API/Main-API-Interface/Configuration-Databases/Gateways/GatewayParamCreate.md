[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayParamCreate

[Previous](GatewayModuleCreate.md) | [Next](GatewayTranslateCreate.md)

# IMTServerAPI::GatewayParamCreate

Create an object of the gateway parameter.
    
    
    IMTConParam*  IMTServerAPI::GatewayParamCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConParam](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConParam::Release](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Release.md) method of this object.
