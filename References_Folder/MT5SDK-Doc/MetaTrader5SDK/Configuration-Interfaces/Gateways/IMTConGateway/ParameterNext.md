[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / ParameterNext

[Previous](ParameterTotal.md) | [Next](ParameterGet.md)

# IMTConGateway::ParameterNext

Get the gateway parameters by the index.

C++
    
    
    MTAPIRES  IMTConGateway::ParameterNext(
       const UINT    pos,       // Position of the parameter
       IMTConParam*  param      // An object of the gateway parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.ParameterNext(
       uint          pos,       // Position of the parameter
       CIMTConParam  param      // An object of the gateway parameter
       )

Python (Manager API)
    
    
    MTConGateway.ParameterNext(
       pos           # Position of the parameter
       )

### Parameters

**pos**  
[in] Position of the gateway, starting with 0.

**param**  
[out] An object of a gateway parameter. The 'param' object must first be created using theIMTAdminAPI::GatewayParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
