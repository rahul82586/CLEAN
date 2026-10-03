[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / Vendor

[Previous](Name.md) | [Next](Description.md)

# IMTConGatewayModule::Vendor

Get the name of the gateway module provider.

C++
    
    
    LPCWSTR  IMTConGatewayModule::Vendor()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGatewayModule.Vendor()

Python (Manager API)
    
    
    MTConGatewayModule.Vendor

### Return Value

If successful, it returns a pointer to a string with the file provider of the gateway module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayModule](../IMTConGatewayModule.md) object.
