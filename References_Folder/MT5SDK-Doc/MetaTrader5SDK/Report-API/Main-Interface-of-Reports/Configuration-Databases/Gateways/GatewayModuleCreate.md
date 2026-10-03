[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayModuleCreate

[Previous](GatewayCreate.md) | [Next](GatewayParamCreate.md)

# IMTReportAPI::GatewayModuleCreate

Create an object of configuration of the gateway module.
    
    
    IMTConGatewayModule*  IMTReportAPI::GatewayModuleCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConGatewayModule](../../../../Configuration-Interfaces/Gateways/IMTConGatewayModule.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConGatewayModule::Release](../../../../Configuration-Interfaces/Gateways/IMTConGatewayModule/Release.md) method of this object.
