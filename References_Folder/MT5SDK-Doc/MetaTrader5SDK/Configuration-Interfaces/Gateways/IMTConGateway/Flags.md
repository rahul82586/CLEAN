[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / Flags

[Previous](Mode.md) | [Next](Timeout.md)

# IMTConGateway::Flags

Get the options of the gateway operation.

C++
    
    
    UINT  IMTConGateway::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnGatewayFlags  CIMTConGateway.Flags()

Python (Manager API)
    
    
    MTConGateway.Flags

### Return Value

A value of the [IMTConGateway::EnGatewayFlags (#engatewayflags)](Enumerations.md#engatewayflags) enumeration.

# IMTConGateway::Flags

Set the options of the gateway operation.

C++
    
    
    MTAPIRES  IMTConGateway::Flags(
       const UINT      flags  // Options of gateway operation
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.Flags(
       EnGatewayFlags  flags  // Options of gateway operation
       )

Python (Manager API)
    
    
    MTConGateway.Flags

### Parameters

**flags**  
[in] To pass the gateway operation options, theIMTConGateway::EnGatewayFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
