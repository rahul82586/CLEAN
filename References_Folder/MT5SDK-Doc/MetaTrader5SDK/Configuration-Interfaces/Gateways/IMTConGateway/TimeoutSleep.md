[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TimeoutSleep

[Previous](TimeoutReconnect.md) | [Next](TimeoutAttempts.md)

# IMTConGateway::TimeoutSleep

Get the timeout between series of reconnections to an external server.

C++
    
    
    UINT  IMTConGateway::TimeoutSleep()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGateway.TimeoutSleep()

Python (Manager API)
    
    
    MTConGateway.TimeoutSleep

### Return Value

Timeout between the series of reconnections to an external server.

# IMTConGateway::TimeoutSleep

Set the timeout between series of reconnections to an external server.

C++
    
    
    MTAPIRES  IMTConGateway::TimeoutSleep(
       const UINT  timeout      // Timeout between reconnection series
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TimeoutSleep(
       uint        timeout      // Timeout between reconnection series
       )

Python (Manager API)
    
    
    MTConGateway.TimeoutSleep

### Parameters

**timeout**  
[in] Timeout between reconnection series.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
