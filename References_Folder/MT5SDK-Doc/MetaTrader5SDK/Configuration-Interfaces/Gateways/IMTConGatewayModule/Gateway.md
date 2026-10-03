[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / Gateway

[Previous](Module.md) | [Next](TradingServer.md)

# IMTConGateway::Gateway

Gets the gateway license module name.

C++
    
    
    LPCWSTR  IMTConGateway::Gateway()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGateway.Gateway()

Python (Manager API)
    
    
    MTConGatewayModule.Gateway

### Return Value

If successful, returns a pointer to the string with the license module name. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayModule](../IMTConGatewayModule.md) object.
