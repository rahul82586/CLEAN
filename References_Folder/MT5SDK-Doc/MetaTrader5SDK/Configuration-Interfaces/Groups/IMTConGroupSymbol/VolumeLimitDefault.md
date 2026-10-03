[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeLimitDefault

[Previous](VolumeLimitExt.md) | [Next](VolumeLimitExtDefault.md)

# IMTConGroupSymbol::VolumeLimitDefault

Gets the default [maximum allowable aggregate volume](../../Symbols/IMTConSymbol/VolumeLimit.md) of positions and orders in one direction for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeLimitDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeLimitDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeLimitDefault

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConGroupSymbol::VolumeLimitExtDefault](VolumeLimitExtDefault.md) method.
