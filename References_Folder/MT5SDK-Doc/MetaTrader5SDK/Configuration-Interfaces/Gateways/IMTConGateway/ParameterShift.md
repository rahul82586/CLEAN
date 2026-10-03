[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / ParameterShift

[Previous](ParameterClear.md) | [Next](ParameterTotal.md)

# IMTConGateway::ParameterShift

Change the position of a gateway parameter in the list.

C++
    
    
    MTAPIRES  IMTConGateway::ParameterShift(
       const UINT  pos,       // Position of the parameter
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.ParameterShift(
       uint        pos,       // Position of the parameter
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConGateway.ParameterShift(
       pos,        # Position of the parameter
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
