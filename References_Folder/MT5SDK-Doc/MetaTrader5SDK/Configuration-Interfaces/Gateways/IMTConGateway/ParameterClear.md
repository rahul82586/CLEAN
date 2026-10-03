[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / ParameterClear

[Previous](ParameterDelete.md) | [Next](ParameterShift.md)

# IMTConGateway::ParameterClear

Clear the list of gateway parameters.

C++
    
    
    MTAPIRES  IMTConGateway::ParameterClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.ParameterClear()

Python (Manager API)
    
    
    MTConGateway.ParameterClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of gateway parameters.
