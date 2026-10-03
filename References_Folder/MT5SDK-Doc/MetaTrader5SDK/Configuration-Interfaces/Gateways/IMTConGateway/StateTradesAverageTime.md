[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / StateTradesAverageTime

[Previous](StateTradesTotal.md) | [Next](../IMTConGatewayModule.md)

# IMTConGateway::StateTradesAverageTime

Get an average time of handling one trade by the gateway.

C++
    
    
    UINT  IMTConGateway::StateTradesAverageTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGateway.StateTradesAverageTime()

Python (Manager API)
    
    
    MTConGateway.StateTradesAverageTime

### Return Value

Average time of handling a trade in milliseconds.

### Note

Handling includes request canformation ([IMTConfirm](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md)) and use of the appropriate trade execution (IMTExecution) after request processing n an external trading system.
