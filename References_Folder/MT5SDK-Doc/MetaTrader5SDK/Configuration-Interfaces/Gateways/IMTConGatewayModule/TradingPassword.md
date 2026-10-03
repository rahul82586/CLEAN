[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / TradingPassword

[Previous](TradingLogin.md) | [Next](Version.md)

# IMTConGatewayModule::TradingPassword

Get a default password that will be used by a gateway to connect to the server.

C++
    
    
    LPCWSTR  IMTConGatewayModule::TradingPassword()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGatewayModule.TradingPassword()

Python (Manager API)
    
    
    MTConGatewayModule.TradingPassword

### Return Value

If successful, it returns a pointer to a string with the default password, which will be used by the gateway to connect to the server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayModule](../IMTConGatewayModule.md) object.
