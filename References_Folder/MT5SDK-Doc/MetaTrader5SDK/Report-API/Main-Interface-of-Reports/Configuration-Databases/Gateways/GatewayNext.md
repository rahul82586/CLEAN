[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayNext

[Previous](GatewayTotal.md) | [Next](GatewayGet.md)

# IMTReportAPI::GatewayNext

Get the gateway configuration by the index.
    
    
    MTAPIRES  IMTReportAPI::GatewayNext(
       const UINT      pos,         // Position of the configuration
       IMTConGateway*  gateway      // Gateway configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**gateway**  
[out] The gateway configuration object. The gateway object must be first created using theIMTReportAPI::GatewayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a gateway with a specified index to the gateway object.
