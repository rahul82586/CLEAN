[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TranslateGetSource

[Previous](TranslateGet.md) | [Next](StateConnected.md)

# IMTConGateway::TranslateGetSource

Gets a price conversion setting applied to the price data transmitted by the gateway based on the specified symbol name in the data source.

C++
    
    
    MTAPIRES  IMTConGateway::TranslateGetSource(
       LPCWSTR                  source,     // The name of the symbol on the data source
       IMTConGatewayTranslate*  param       // An object of data conversion setting
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TranslateGetSource(
       string                   source,     // The name of the symbol on the data source
       CIMTConGatewayTranslate  param       // An object of data conversion setting
       )

Python (Manager API)
    
    
    MTConGateway.TranslateGetSource(
       source                   # The name of the symbol on the data source
       )

### Parameters

**source**  
[in] The name of a symbol in a data feed.

**param**  
[out] An object of data conversion setting. The 'param' object must first be created using theIMTAdminAPI::GatewayTranslateCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
