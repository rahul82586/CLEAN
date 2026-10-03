[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProvider](../IMTProvider.md) / IMTProvider Version

[Previous](IMTProvider-Module.md) | [Next](../IMTProviderArray.md)

# IMTECNProvider::Version

Get the version of the gateway through which the order is forwarded to the external system.

C++
    
    
    UINT  IMTECNProvider::Version()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNProvider.Version()

### Return Value

Gateway module version.

### Note

The [IMTConGatewayModule::Version](../../../Configuration-Interfaces/Gateways/IMTConGatewayModule/Version.md) value is used for the version.
