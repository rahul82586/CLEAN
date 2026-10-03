[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConGatewayModule::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConGatewayModule::Assign(
       const IMTConGatewayModule*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGatewayModule.Assign(
       CIMTConGatewayModule        param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
