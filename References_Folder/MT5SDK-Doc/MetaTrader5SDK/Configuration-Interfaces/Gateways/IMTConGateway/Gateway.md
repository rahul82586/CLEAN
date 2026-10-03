[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / Gateway

[Previous](TradingPassword.md) | [Next](GatewayServer.md)

# IMTConGateway::Gateway

Gets the gateway license module name.

C++
    
    
    LPCWSTR  IMTConGateway::Gateway()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGateway.Gateway()

Python (Manager API)
    
    
    MTConGateway.Gateway

### Return Value

If successful, returns a pointer to the string with the license module name. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGateway](../IMTConGateway.md) object.
