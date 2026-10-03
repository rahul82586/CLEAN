[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / ParameterNext

[Previous](ParameterTotal.md) | [Next](ParameterGet.md)

# IMTConGatewayModule::ParameterNext

Get the gateway module parameters by the index.

C++
    
    
    MTAPIRES  IMTConGatewayModule::ParameterNext(
       const UINT    pos,       // Position of a gateway
       IMTConParam*  param      // An object of the gateway module parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGatewayModule.ParameterNext(
       uint          pos,       // Position of a gateway
       CIMTConParam  param      // An object of the gateway module parameter
       )

Python (Manager API)
    
    
    MTRetCode  CIMTConGatewayModule.ParameterNext(
       pos           # Position of a gateway
       )

### Parameters

**pos**  
[in] Position of the gateway, starting with 0.

**param**  
[out] An object of the gateway module parameter. The 'param' object must first be created using theIMTAdminAPI::GatewayParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the parameters of a gateway module with a specified index to the param object.
