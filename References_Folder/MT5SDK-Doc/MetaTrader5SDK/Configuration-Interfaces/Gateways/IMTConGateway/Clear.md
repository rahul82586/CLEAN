[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConGateway::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConGateway::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.Clear()

Python (Manager API)
    
    
    MTConGateway.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
