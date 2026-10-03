[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProvider](../IMTProvider.md) / IMTProvider Name

[Previous](IMTProvider-ProviderID.md) | [Next](IMTProvider-Module.md)

# IMTECNProvider::Name

Get the name of the provider through which the order is forwarded to the external system.

C++
    
    
    LPCWSTR  IMTECNProvider::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNProvider.Name()

### Return Value

Provider name.

### Note

A gateway or MetaTrader 5 cluster is used as a provider.
