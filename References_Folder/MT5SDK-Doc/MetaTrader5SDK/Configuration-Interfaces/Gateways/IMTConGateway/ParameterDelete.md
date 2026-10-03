[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / ParameterDelete

[Previous](ParameterUpdate.md) | [Next](ParameterClear.md)

# IMTConGateway::ParameterDelete

Delete a gateway parameter by the index.

C++
    
    
    MTAPIRES  IMTConGateway::ParameterDelete(
       const UINT  pos      // Position of the parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.ParameterDelete(
       uint        pos      // Position of the parameter
       )

Python (Manager API)
    
    
    MTConGateway.ParameterDelete(
       pos         # Position of the parameter
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
