[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConGateway::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConGateway::Assign(
       const IMTConGateway*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.Assign(
       CIMTConGateway        param      // Source object
       )

### Parameters

**param**  
Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
