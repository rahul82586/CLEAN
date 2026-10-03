[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TranslateNext

[Previous](TranslateTotal.md) | [Next](TranslateGet.md)

# IMTConGateway::TranslateNext

Get a setting of conversion of price data transmitted by the gateway by the index.

C++
    
    
    MTAPIRES  IMTConGateway::TranslateNext(
       const UINT               pos,       // Position of a gateway
       IMTConGatewayTranslate*  param      // An object of data conversion setting
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TranslateNext(
       uint                     pos,       // Position of a gateway
       CIMTConGatewayTranslate  param      // An object of data conversion setting
       )

Python (Manager API)
    
    
    MTConGateway.TranslateNext(
       pos                      # Position of a gateway
       )

### Parameters

**pos**  
[in] Position of the gateway, starting with 0.

**param**  
[out] An object of data conversion setting. The 'param' object must first be created using theIMTAdminAPI::GatewayTranslateCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
