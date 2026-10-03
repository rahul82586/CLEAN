[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / TradingLogin

[Previous](TradingServer.md) | [Next](TradingPassword.md)

# IMTConGatewayModule::TradingLogin

Get a default login that will be used by a gateway to connect to the server.

C++
    
    
    LPCWSTR  IMTConGatewayModule::TradingLogin()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGatewayModule.TradingLogin()

Python (Manager API)
    
    
    MTConGatewayModule.TradingLogin

### Return Value

If successful, it returns a pointer to a string with the default login, which will be used by the gateway to connect to the server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayModule](../IMTConGatewayModule.md) object.
