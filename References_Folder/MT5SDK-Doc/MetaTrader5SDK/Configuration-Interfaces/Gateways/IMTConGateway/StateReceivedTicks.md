[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / StateReceivedTicks

[Previous](StateConnected.md) | [Next](StateReceivedBooks.md)

# IMTConGateway::StateReceivedTicks

Request number of price changes ([MTTick](../../../Structures/MTTick.md)) received by the gateway from an external trading system during the current session.

C++
    
    
    UINT  IMTConGateway::StateReceivedTicks()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGateway.StateReceivedTicks()

Python (Manager API)
    
    
    MTConGateway.StateReceivedTicks

### Return Value

Number of price changes.
