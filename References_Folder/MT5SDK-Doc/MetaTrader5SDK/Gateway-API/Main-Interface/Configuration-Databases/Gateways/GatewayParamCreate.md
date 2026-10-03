[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayParamCreate

[Previous](GatewayCreate.md) | [Next](GatewayTranslateCreate.md)

# IMTGatewayAPI::GatewayParamCreate

Create an object of the gateway parameter.

C++
    
    
    IMTConParam*  IMTGatewayAPI::GatewayParamCreate()

.NET
    
    
    CIMTConParam  CIMTGatewayAPI.GatewayParamCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConParam](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConParam::Release](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Release.md) method of this object.
