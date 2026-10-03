[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TranslateGet

[Previous](TranslateNext.md) | [Next](TranslateGetSource.md)

# IMTConGateway::TranslateGet

Gets a price conversion setting applied to the price data transmitted by the gateway based on the specified symbol name in the trading platform.

C++
    
    
    MTAPIRES  IMTConGateway::TranslateGet(
       LPCWSTR                  symbol,     // Symbol name
       IMTConGatewayTranslate*  param       // An object of data conversion setting
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TranslateGet(
       string                   symbol,     // Symbol name
       CIMTConGatewayTranslate  param       // An object of data conversion setting
       )

Python (Manager API)
    
    
    MTConGateway.TranslateGet()

### Parameters

**symbol**  
[in] Symbol name.

**param**  
[out] An object of data conversion setting. The 'param' object must first be created using theIMTAdminAPI::GatewayTranslateCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConGatewayTranslate::Symbol](../IMTConGatewayTranslate/Symbol.md) value is used as the symbol.
