[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerRange](../IMTConServerRange.md) / UsedTo

[Previous](UsedFrom.md) | [Next](../IMTConServerAddressRange.md)

# IMTConServerRange::UsedTo

Get the end of the range of accounts, orders or deals already used on a trade server.

C++
    
    
    UINT64  IMTConServerRange::UsedTo()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConServerRange.UsedTo()

Python (Manager API)
    
    
    MTConServerRange.UsedTo

### Return Value

The end of the range of accounts, orders or deals already used on a trade server.

### Note

The range information is updated in the configuration once an hour.
