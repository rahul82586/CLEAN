[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / ParameterAdd

[Previous](TimeoutAttempts.md) | [Next](ParameterUpdate.md)

# IMTConGateway::ParameterAdd

Add a gateway parameter.

C++
    
    
    MTAPIRES  IMTConGateway::ParameterAdd(
       IMTConParam*  param      // An object of the gateway parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.ParameterAdd(
       CIMTConParam  param      // An object of the gateway parameter
       )

Python (Manager API)
    
    
    MTConGateway.ParameterAdd(
       param         # An object of the gateway parameter
       )

### Parameters

**param**  
[in] An object of the gateway parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
