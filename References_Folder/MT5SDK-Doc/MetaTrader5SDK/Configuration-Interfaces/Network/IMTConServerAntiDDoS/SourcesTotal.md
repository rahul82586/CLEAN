[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / SourcesTotal

[Previous](SourcesShift.md) | [Next](SourcesNext.md)

# IMTConServerAntiDDoS::SourcesTotal

Get the number of ranges of IP addresses of Anti DDoS provider's proxy servers.

C++
    
    
    UINT  IMTConServerAntiDDoS::SourcesTotal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerAntiDDoS.SourcesTotal()

Python (Manager API)
    
    
    MTConServerAntiDDoS.SourcesTotal()

### Return Value

The number of ranges of IP addresses.

### Note

The ranges of IP addresses of proxy servers should be provide by your Anti DDoS protection service provider. The ranges are used as an additional protection measure: connections forwarded by the Anti-DDoS provider will only be accepted from these addresses.
