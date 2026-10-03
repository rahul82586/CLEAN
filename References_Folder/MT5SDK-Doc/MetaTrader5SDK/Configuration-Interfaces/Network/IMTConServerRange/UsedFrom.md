[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerRange](../IMTConServerRange.md) / UsedFrom

[Previous](To.md) | [Next](UsedTo.md)

# IMTConServerRange::UsedFrom

Get the beginning of the range of accounts, orders or deals already used on a trade server.

C++
    
    
    UINT64  IMTConServerRange::UsedFrom()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConServerRange.UsedFrom()

Python (Manager API)
    
    
    MTConServerRange.UsedFrom

### Return Value

The beginning of the range of accounts, orders or deals already used on a trade server.

### Note

The range information is updated in the configuration once an hour.
