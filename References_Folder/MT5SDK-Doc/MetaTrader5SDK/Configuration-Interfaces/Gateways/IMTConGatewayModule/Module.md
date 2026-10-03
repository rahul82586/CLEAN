[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / Module

[Previous](Description.md) | [Next](Gateway.md)

# IMTConGatewayModule::Module

Get the name of the gateway module file.

C++
    
    
    LPCWSTR  IMTConGatewayModule::Module()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGatewayModule.Module()

Python (Manager API)
    
    
    MTConGatewayModule.Module

### Return Value

If successful, it returns a pointer to a string with the file name of the gateway module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayModule](../IMTConGatewayModule.md) object.
