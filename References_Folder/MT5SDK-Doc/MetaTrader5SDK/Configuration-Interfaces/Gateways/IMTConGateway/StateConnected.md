[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / StateConnected

[Previous](TranslateGetSource.md) | [Next](StateReceivedTicks.md)

# IMTConGateway::StateConnected

Get the state of the gateway connection to an external trading system.

C++
    
    
    bool  IMTConGateway::StateConnected()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConGateway.StateConnected()

Python (Manager API)
    
    
    MTConGateway.StateConnected

### Return Value

If the gateway has successfully connected to an external trading system and is ready to interact with it, the method returns TRUE, otherwise — FALSE.
