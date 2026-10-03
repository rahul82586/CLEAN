[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProvider](../IMTProvider.md) / IMTProvider Module

[Previous](IMTProvider-Name.md) | [Next](IMTProvider-Version.md)

# IMTECNProvider::Module

Get the name of the gateway through which the order is forwarded to the external system.

C++
    
    
    LPCWSTR  IMTECNProvider::Module()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNProvider.Module()

### Return Value

Gateway module name.

### Note

The [IMTConGateway::Module](../../../Configuration-Interfaces/Gateways/IMTConGateway/Module.md) value is used as the name.
