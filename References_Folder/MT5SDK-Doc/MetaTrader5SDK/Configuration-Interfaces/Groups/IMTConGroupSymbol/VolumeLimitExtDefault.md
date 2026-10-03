[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeLimitExtDefault

[Previous](VolumeLimitDefault.md) | [Next](MarginFlags.md)

# IMTConGroupSymbol::VolumeLimitExtDefault

Gets [the default maximum aggregate volume](../../Symbols/IMTConSymbol/VolumeLimit.md) of positions and orders for a symbol with extended accuracy. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeLimitExtDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeLimitExtDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeLimitExtDefault

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeLimitDefault](VolumeLimitDefault.md) method.
