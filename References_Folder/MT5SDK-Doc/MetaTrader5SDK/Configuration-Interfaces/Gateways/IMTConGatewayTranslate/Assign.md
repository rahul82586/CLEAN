[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayTranslate](../IMTConGatewayTranslate.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConGatewayTranslate::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConGatewayTranslate::Assign(
       const IMTConGatewayTranslate*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGatewayTranslate.Assign(
       CIMTConGatewayTranslate        param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
