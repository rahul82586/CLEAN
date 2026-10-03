[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / Name

[Previous](Clear.md) | [Next](Vendor.md)

# IMTConGatewayModule::Name

Get the gateway name, which is inserted by default to a configuration when selecting this module.

C++
    
    
    LPCWSTR  IMTConGatewayModule::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGatewayModule.Name()

Python (Manager API)
    
    
    MTConGatewayModule.Name

### Return Value

If successful, it returns a pointer to a string with the default name of the gateway. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayModule](../IMTConGatewayModule.md) object.
