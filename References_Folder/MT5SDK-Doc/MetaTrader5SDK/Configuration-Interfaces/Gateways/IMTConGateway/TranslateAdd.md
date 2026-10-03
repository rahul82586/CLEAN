[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TranslateAdd

[Previous](GroupNext.md) | [Next](TranslateUpdate.md)

# IMTConGateway::TranslateAdd

Add a setting of the price data transmitted by the gateway.

C++
    
    
    MTAPIRES  IMTConGateway::TranslateAdd(
       IMTConGatewayTranslate*  param      // An object of data conversion setting
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TranslateAdd(
       CIMTConGatewayTranslate  param      // An object of data conversion setting
       )

Python (Manager API)
    
    
    MTConGateway.TranslateAdd(
        param                   # An object of data conversion setting
       )

### Parameters

**param**  
[in] An object of data conversion setting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
