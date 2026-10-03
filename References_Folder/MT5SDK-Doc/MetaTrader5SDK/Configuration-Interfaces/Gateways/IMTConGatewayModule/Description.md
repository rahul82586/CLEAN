[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / Description

[Previous](Vendor.md) | [Next](Module.md)

# IMTConGatewayModule::Description

Get the description of a gateway module.

C++
    
    
    LPCWSTR  IMTConGatewayModule::Description()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGatewayModule.Description()

Python (Manager API)
    
    
    MTConGatewayModule.Description

### Return Value

If successful, it returns a pointer to a string with the description of a gateway module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayModule](../IMTConGatewayModule.md) object.
