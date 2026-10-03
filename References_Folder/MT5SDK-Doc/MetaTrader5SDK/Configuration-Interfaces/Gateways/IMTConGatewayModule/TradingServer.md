[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / TradingServer

[Previous](Gateway.md) | [Next](TradingLogin.md)

# IMTConGatewayModule::TradingServer

Get the default address of the server to which the gateway module will connect.

C++
    
    
    LPCWSTR  IMTConGatewayModule::TradingServer()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGatewayModule.TradingServer()

Python (Manager API)
    
    
    MTConGatewayModule.TradingServer

### Return Value

If successful, it returns a pointer to a string with the default address of the server to which the gateway module will connect. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayModule](../IMTConGatewayModule.md) object.
