[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / Mode

[Previous](GatewayPassword.md) | [Next](Flags.md)

# IMTConGateway::Mode

Get the gateway operation mode.

C++
    
    
    UINT  IMTConGateway::Mode()  const

.NET (Gateway/Manager API)
    
    
    EnGatewayMode  CIMTConGateway.Mode()

Python (Manager API)
    
    
    MTConGateway.Mode

### Return Value

One of the values of the [IMTConGateway::EnGatewayMode (#engatewaymode)](Enumerations.md#engatewaymode) enumeration.

# IMTConGateway::Mode

Set the gateway operation mode.

C++
    
    
    MTAPIRES  IMTConGateway::Mode(
       const UINT     mode   // Operation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.Mode(
       EnGatewayMode  mode   // Operation mode
       )

Python (Manager API)
    
    
    MTConGateway.Mode

### Parameters

**mode**  
[in] TheIMTConGateway::EnGatewayModeenumeration is used to pass the operation mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
