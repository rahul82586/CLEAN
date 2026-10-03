[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / ParameterGet

[Previous](ParameterNext.md) | [Next](SymbolAdd.md)

# IMTConGateway::ParameterGet

Get the gateway parameter by the name.

C++
    
    
    MTAPIRES  IMTConGateway::ParameterGet(
       LPCWSTR       name,      // Parameter name
       IMTConParam*  param      // An object of the gateway parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.ParameterGet(
       string        name,      // Parameter name
       CIMTConParam  param      // An object of the gateway parameter
       )

Python (Manager API)
    
    
    MTConGateway.ParameterGet()

### Parameters

**name**  
[in] Parameter Name.

**param**  
[out] An object of a gateway parameter. The 'param' object must first be created using theIMTAdminAPI::GatewayParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConParam::Name](../../Additional-Parameters/IMTConParam/Name.md) value is used as the parameter name.
