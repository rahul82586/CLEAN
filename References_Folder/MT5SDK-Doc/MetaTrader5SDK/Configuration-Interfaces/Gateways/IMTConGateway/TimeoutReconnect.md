[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TimeoutReconnect

[Previous](Timeout.md) | [Next](TimeoutSleep.md)

# IMTConGateway::TimeoutReconnect

Get timeout to wait between attempts to reconnect to an external server.

C++
    
    
    UINT  IMTConGateway::TimeoutReconnect()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGateway.TimeoutReconnect()

Python (Manager API)
    
    
    MTConGateway.TimeoutReconnect

### Return Value

Timeout to wait between attempts to reconnect to an external server.

# IMTConGateway::TimeoutReconnect

Set the timeout to wait between attempts to reconnect to an external server.

C++
    
    
    MTAPIRES  IMTConGateway::TimeoutReconnect(
       const UINT  timeout      // Timeout between reconnections
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TimeoutReconnect(
       uint        timeout      // Timeout between reconnections
       )

Python (Manager API)
    
    
    MTConGateway.TimeoutReconnect

### Parameters

**timeout**  
[in] Timeout between reconnections.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
