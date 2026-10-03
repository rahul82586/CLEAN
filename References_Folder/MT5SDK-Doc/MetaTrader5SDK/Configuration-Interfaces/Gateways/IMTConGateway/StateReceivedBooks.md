[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / StateReceivedBooks

[Previous](StateReceivedTicks.md) | [Next](StateTrafficIn.md)

# IMTConGateway::StateReceivedBooks

Request number of the Depth of Market changes ([MTBookDiff](../../../Structures/MTBookMTBookDiff.md)) received by the gateway from an external trading system during the current session.

C++
    
    
    UINT  IMTConGateway::StateReceivedBooks()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGateway.StateReceivedBooks()

Python (Manager API)
    
    
    MTConGateway.StateReceivedBooks

### Return Value

Number of Depth of Market changes.
