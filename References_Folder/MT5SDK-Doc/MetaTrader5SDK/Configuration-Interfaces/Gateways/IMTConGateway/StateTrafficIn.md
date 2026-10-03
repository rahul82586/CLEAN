[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / StateTrafficIn

[Previous](StateReceivedBooks.md) | [Next](StateTrafficOut.md)

# IMTConGateway::StateTrafficIn

Request traffic volume received by the gateway during the current session.

C++
    
    
    UINT  IMTConGateway::StateTrafficIn()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGateway.StateTrafficIn()

Python (Manager API)
    
    
    MTConGateway.StateTrafficIn

### Return Value

Incoming traffic volume in bytes.
