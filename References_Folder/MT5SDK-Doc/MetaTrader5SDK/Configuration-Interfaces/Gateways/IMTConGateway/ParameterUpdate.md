[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / ParameterUpdate

[Previous](ParameterAdd.md) | [Next](ParameterDelete.md)

# IMTConGateway::ParameterUpdate

Update a gateway parameter.

C++
    
    
    MTAPIRES  IMTConGateway::ParameterUpdate(
       const UINT          pos,       // Position of the parameter
       const IMTConParam*  param      // An object of the gateway parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.ParameterUpdate(
       uint                pos,       // Position of the parameter
       CIMTConParam        param      // An object of the gateway parameter
       )

Python (Manager API)
    
    
    MTConGateway.ParameterUpdate(
       pos,                # Position of the parameter
       param               # An object of the gateway parameter
       )
    
    
    MTConGateway.ParameterSet(
       parameter_list      # A list of gateway parameters
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**param**  
[in] An object of the gateway parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
