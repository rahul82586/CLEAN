[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / ParameterGet

[Previous](ParameterNext.md) | [Next](../IMTConGatewayTranslate.md)

# IMTConGatewayModule::ParameterGet

Get the gateway module parameter by the name.

C++
    
    
    MTAPIRES  IMTConGatewayModule::ParameterGet(
       LPCWSTR       name,      // Parameter name
       IMTConParam*  param      // An object of the gateway parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGatewayModule.ParameterGet(
       string        name,      // Parameter name
       CIMTConParam  param      // An object of the gateway parameter
       )

Python (Manager API)
    
    
    MTConGatewayModule.ParameterGet(
       name          # Parameter name
       )
    
    
    MTConGatewayModule.ParameterGet()

### Parameters

**name**  
[in] Parameter Name.

**param**  
[out] An object of a gateway parameter. The 'param' object must first be created using theIMTAdminAPI::GatewayParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConParam::Name](../../Additional-Parameters/IMTConParam/Name.md) value is used as the parameter name.
