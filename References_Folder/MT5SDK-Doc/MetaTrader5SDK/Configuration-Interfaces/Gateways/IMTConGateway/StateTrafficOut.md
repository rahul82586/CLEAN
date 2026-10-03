[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / StateTrafficOut

[Previous](StateTrafficIn.md) | [Next](StateTradesTotal.md)

# IMTConGateway::StateTrafficOut

Request traffic volume sent by the gateway during the current session.

C++
    
    
    UINT  IMTConGateway::StateTrafficOut()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGateway.StateTrafficOut()

Python (Manager API)
    
    
    MTConGateway.StateTrafficOut

### Return Value

Outgoing traffic volume in bytes.
