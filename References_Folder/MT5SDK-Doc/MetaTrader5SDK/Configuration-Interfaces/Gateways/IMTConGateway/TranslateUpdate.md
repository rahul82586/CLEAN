[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TranslateUpdate

[Previous](TranslateAdd.md) | [Next](TranslateDelete.md)

# IMTConGateway::TranslateUpdate

Update the price data conversion settings of a gateway.

C++
    
    
    MTAPIRES  IMTConGateway::TranslateUpdate(
       const UINT                     pos,       // Setting position
       const IMTConGatewayTranslate*  param      // An object of data conversion setting
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TranslateUpdate(
       uint                           pos,       // Setting position
       CIMTConGatewayTranslate        param      // An object of data conversion setting
       )

Python (Manager API)
    
    
    MTConGateway.TranslateUpdate(
       pos,                           # Setting position
       param                          # An object of data conversion setting
       )
    
    
    MTConGateway.TranslateSet(
       param_list                     # A list of data conversion settings
       )

### Parameters

**pos**  
[in] Setting position, starting with 0.

**param**  
[in] An object of data conversion setting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
