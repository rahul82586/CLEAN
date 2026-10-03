[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayModuleNext

[Previous](GatewayModuleGet.md) | [Next](../Subscriptions.md)

# IMTReportAPI::GatewayModuleNext

Get the gateway module by the index.
    
    
    MTAPIRES  IMTReportAPI::GatewayModuleNext(
       const UINT            pos,        // Position of the module
       IMTConGatewayModule*  module      // Object of the gateway module configuration
       )

### Parameters

**pos**  
[in] Position of the module, starting with 0.

**module**  
[out] The gateway module object. The module object must be first created using theIMTReportAPI::GatewayModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the gateway configuration with a specified index to the module object.
