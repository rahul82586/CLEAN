[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProvider](../IMTProvider.md) / IMTProvider ProviderID

[Previous](IMTProvider-ID.md) | [Next](IMTProvider-Name.md)

# IMTECNProvider::ProviderID

Get the ID of the provider through which the order is forwarded to the external system.

C++
    
    
    UINT64  IMTECNProvider::ProviderID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNProvider.ProviderID()

### Return Value

Provider ID.

### Note

A gateway or MetaTrader 5 cluster is used as a provider.
