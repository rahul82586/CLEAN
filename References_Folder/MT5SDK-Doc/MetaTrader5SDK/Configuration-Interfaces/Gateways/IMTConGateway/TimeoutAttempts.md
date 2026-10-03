[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TimeoutAttempts

[Previous](TimeoutSleep.md) | [Next](ParameterAdd.md)

# IMTConGateway::TimeoutAttempts

Get the number of attempts in the series of reconnections to the external server.

C++
    
    
    UINT  IMTConGateway::TimeoutAttempts()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGateway.TimeoutAttempts()

Python (Manager API)
    
    
    MTConGateway.TimeoutAttempts

### Return Value

The number of attempts in a series of reconnections.

# IMTConGateway::TimeoutAttempts

The number of attempts in the series of reconnections to the external server.

C++
    
    
    MTAPIRES  IMTConGateway::TimeoutAttempts(
       const UINT  attempts      // The number of attempts in a series of reconnections
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TimeoutAttempts(
       uint        attempts      // The number of attempts in a series of reconnections
       )

Python (Manager API)
    
    
    MTConGateway.TimeoutAttempts

### Parameters

**attempts**  
[in] The number of attempts in a series of reconnections.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
