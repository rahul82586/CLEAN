[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayTranslateCreate

[Previous](GatewayParamCreate.md) | [Next](GatewaySubscribe.md)

# IMTServerAPI::GatewayTranslateCreate

Create an object of the parameter for converting the information received by the gateway.
    
    
    IMTConGatewayTranslate*  IMTServerAPI::GatewayTranslateCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConGatewayTranslate](../../../../Configuration-Interfaces/Gateways/IMTConGatewayTranslate.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConGatewayTranslate::Release](../../../../Configuration-Interfaces/Gateways/IMTConGatewayTranslate/Release.md) method of this object.
