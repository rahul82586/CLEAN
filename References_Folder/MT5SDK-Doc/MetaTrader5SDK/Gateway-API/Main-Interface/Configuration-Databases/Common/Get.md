[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Get

[Previous](Unsubscribe.md) | [Next](../Data-Feeds.md)

# IMTGatewayAPI::CommonGet

Get the common platform configuration.

C++
    
    
    MTAPIRES  IMTGatewayAPI::CommonGet(
       IMTConCommon*  common      // Configuration
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.CommonGet(
       CIMTConCommon  common      // Configuration
       )

### Parameters

**common**  
[out] A common configuration object. The object must first be created using theIMTGatewayAPI::CommonCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is not available for data feeds.
